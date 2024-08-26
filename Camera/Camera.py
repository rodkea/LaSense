from picamera2 import Picamera2
from PyQt5.QtCore import pyqtSlot
from .ConfigEnums import Resolution
from picamera2.encoders import H264Encoder, Quality, Encoder
from datetime import datetime
from Signals import Signals
from config import ConfigType
import os


class Camera(Picamera2):
  """A class representing the PiCam V2

  Inherits from Picamera2    
  """

  USER_CONFIG_PATH = "config/user.config"
  DEFAULT_CONFIG_PATH = "config/default.config"

  def __init__(self, resolution : Resolution, signals : Signals):
      super().__init__()        
      self._encoder = H264Encoder()  
      self._signals = signals
      # SLOTS
      self._signals.on_change_brightness.connect(self._change_brightness)  
      self._signals.on_change_contrast.connect(self._change_contrast)    
      self._signals.on_change_iso.connect(self._change_iso)   
      self._signals.on_change_saturation.connect(self._change_saturation)   
      self._signals.on_change_sharpness.connect(self._change_sharpness)
      self._signals.on_set_user_settings.connect(self.change_user_config)
      self._signals.on_recording_signal.connect(self.start_recording)
      self._signals.on_stop_recording_signal.connect(self.stop_recording)
      video_config = self.create_video_configuration(
          main = {"size" : (1920, 1080), "format": 'YUV420'}, encode="main"                             
      )
      self.align_configuration(video_config)
      self.configure(video_config)

  @property
  def user_config(self):
      return self._user_config
  
  @property
  def default_config(self):
      return self._default_config

  def _read_config_file(self, file_path : str) -> ConfigType:
      """Read configuration settings from a file and returns them as a dictionary.

      Args:
          file_path(str): The path to the configuration file.
      
      Returns:
          ConfigType: A dictionary containing the configuration setings read from the file.
      """

      config_dict : ConfigType = {}
      types = {
          "AnalogueGain" : float,
          "Brightness" : float,
          "Contrast" : float,
          "NoiseReductionMode" : int,        
          "Saturation" : float,
          "Sharpness" : float,
          "BaseName" : str,
      }
      with open(file_path, 'r') as file:
          for line in file:
              key, value = line.strip().split('=')
              config_dict[key] = types[key](value)
      return config_dict

  def write_config_file(self, file_path : str, config : dict):
      """Writes configuration settings from a dictionary to a file.
      
      Args:
          file_path (str): The path to the configuration file.
          config (dict): A dictionary containing the configuration settins to be written to the file.

      Returns:
          None
      """
      with open(file_path, 'w') as file:
          for key, value in config.items():
              file.write(f"{key}={value}\n")
          # Remove the last \n from file            
          if config:
              file.seek(file.tell() - 1, 0)
              file.truncate()
              
    
  def _change_brightness(self, value : int):
      """Changes the brightness setting of the camera.

      This method adjusts the brightness setting of the camera to the specified value where
      -1.0 is very dark, 1.0 is very bright, and 0.0 is de default "normal" brightness.
      If the provided value is greater than 1.0, the brightness setting is set to 1.0.
      If the provided value is less than -1.0, the brightness setting is set to -1.0.
      Otherwise, the brightness setting is set to the provided value.
      

      Args:
          value (float): The desired brightness value. Must be between -1.0 and 1.0.

      Returns:
          None
      """
      value = (value - 50 ) / 100.0
      if value > 1.0:
          self.set_controls({"Brightness" : 1.0})        
      elif value < -1.0:
          self.set_controls({"Brightness" : -1.0})
      else:
          self.set_controls({"Brightness" : value})        

  def _change_contrast(self, value: int):
      """Changes the brightness setting of the camera.

      This method adjusts the contrast setting of the camera to the specified value where
      0.0 means "no contrast", 1.0 is the default "normal" contrast, and larger values 
      increase the contrast proportinally.
      If the provided value is greater than 320, the contrast setting is set to 32.0.
      If the provided value is less than 0, the contrast setting is set to 0.0.
      Otherwise, the contrast setting is set to the provided value divided by 10.0.
      

      Args:
          value (int): The desired contrast value. Must be between 0 and 320.

      Returns:
          None
      """
      value = value / 10.0
      if value > 32.0:
          self.set_controls({"Contrast" : 32.0})
      elif value < 0.0:
          self.set_controls({"Contrast" : 0.0})
      else:
          self.set_controls({"Contrast" : value})

  def _change_iso(self, value : int):
      """Changes the analogue gain setting of the camera.

      This method adjusts the analogue gain setting of the camera to the specified value.         
      If the provided value is greater than 106, the gain setting is set to 10.6.
      If the provided value is less than 0, the gain setting is set to 0.0.
      Otherwise, the gain setting is set to the provided value.
      

      Args:
          value (int): The desired gain value. Must be between 0 and 106.

      Returns:
          None
      """
      value = value / 10.0
      if value > 10.6:
          self.set_controls({"AnalogueGain" : 10.6})
      elif value < 0.0:
          self.set_controls({"AnalogueGain" : 0.0})
      else:
          self.set_controls({"AnalogueGain" : value})            

  def _change_noise_reduction(self, mode : int):
      """Changes the noise reduction mode of the camera.

      This method adjusts the noise reduction mode of the camera to the specified value.
      If the provided mode is less than 0 or greater than 2, the noise reduction mode is set to 'HighQuality' (2).        
      Otherwise, the noise reduction mode is set according to the provided value:
          - 0: 'Off' - No noise reduction.
          - 1: 'Fast' - Fast noise reduction.
          - 2: 'HighQuality' - Best noise reduction.

      Args:
          mode (int): The desired noise reduction mode.
              Must be one of the following values: 0 (Off), 1 (Fast), or 2 (HighQuality).

      Returns:
          None
      """
      if mode > 2 or mode < 0:        
          self.set_controls({"NoiseReductionMode" : 2})            
      else:
          self.set_controls({"NoiseReductionMode" : mode})            

  def _change_saturation(self, value : int):
      """Changes the saturation setting of the camera.

      This method adjusts the amount of colour saturation to the specified value 
      where 0.0 produces greyscale images, 1.0 represens default "normal" saturation, and
      higher values produce more saturated colours.
      If the provided value is greater than 320, the saturation setting is set to 32.0.
      If the provided value is less than 0, the saturation setting is set to 0.0.
      Otherwise, the saturation setting is set to the provided value.

      Args:
          value (int): The desired saturation value. Must be between 0 and 320.

      Returns:
          None
      """
      value = value / 10.0
      if value > 32.0:
          self.set_controls({"Saturation" : 32.0})
      elif value < 0.0:
          self.set_controls({"Saturation" : 0.0})
      else:
          self.set_controls({"Saturation" : value})

  def _change_sharpness(self, value : int):
      """Changes the sharpness setting of the camera.

      This method adjusts the amount of image sharpness to the specified value 
      where 0.0 implies no additional sharpering is performed, 1.0 represens default "normal" 
      sharpness,and larger values aplly poportionately stronger sharpening.
      If the provided value is greater than 160, the sharpness setting is set to 16.0.
      If the provided value is less than 0, the sharpness setting is set to 0.0.
      Otherwise, the sharpness setting is set to the provided value.

      Args:
          value (int): The desired sharpness value. Must be between 00 and 160.

      Returns:
          None
      """
      value = value / 10.0
      if value > 16.0:
          self.set_controls({"Sharpness" : 16.0})
      elif value < 0.0:
          self.set_controls({"Sharpness" : 0.0})
      else:
          self.set_controls({"Sharpness" : value})

  def change_user_config(self, config : dict):
      """Changes the user configuration settings of the camera.

      This method updates the user configuration settings of the camera with the provided dictionary.
      The updated settings are then written to the user configuration file.

      Args:
          config (dict): A dictionary containing the updated user configuration settings.

      Returns:
          None
      """
      self._user_config = config
      self.set_controls({ key:value for key, value in self.user_config.items() if key != "BaseName" })
      
  
  def _change_resolution(self, mode : int):
      """Changes the size (width and height) of output image.
      If the provided mode is less than 0 or greater than 2, the resolution is set to 1920x1080 .        
      Otherwise, the resolution mode is set according to the provided value:
          - 0: 640x480.
          - 1: 1640x1232.
          - 2: 1920x1080.
      Args:
          mode (int): The desired resolution mode.
              Must be one of the following values: 0 (640x480), 1 (1640x1232), or 2 (1920x1080).
      Returns:
          None        
      """
      if mode == 0:
          self.video_configuration.size((640, 480))
      if mode == 1:
          self.video_configuration.size((1640, 1232))
      else:
          self.video_configuration.size((1920, 1080))

  def start_recording(self):
      current_datetime = datetime.now().strftime("%d%m%y-%H%M")              
      if not os.path.exists(f"outputs/{self.user_config['BaseName']}-{current_datetime}.yuv"):
          output = f"outputs/{self.user_config['BaseName']}-{current_datetime}.yuv"
      else:    
          count = 1           
          while True:                                
              if not os.path.exists(f"outputs/{self.user_config['BaseName']}-{current_datetime}({count}).yuv"):                    
                  output = f"outputs/{self.user_config['BaseName']}-{current_datetime}({count}).yuv"
                  break                
              count += 1
      self.start_encoder(self._encoder, output, quality=Quality.VERY_HIGH)

  def stop_recording(self):
      self.stop_encoder()
  