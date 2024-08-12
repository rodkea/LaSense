from enum import Enum

class Resolution(Enum):
    """
    An enumeration representing different screen resolutions for Picamer V2 (on video).

    Attributes:
        FHD: Full High Definition with a width of 1920 pixels and a height of 1080 pixels.
        HD: High Definition with a width of 1280 pixels and a height of 720 pixels.
        STD_VGA: Standard VGA with a width of 640 pixels and a height of 480 pixels.        
    """
    FHD = (1920, 1080)
    HD = (1280, 720)
    STD_VGA = (640, 480)
    
    def __iter__(self):
        return iter(self.value)
    
    def __getitem__(self, index):
        return self.value[index]
    
    def __repr__(self) -> str:
        return f"({self.value[0],self.value[1]})"
    
    def __str__(self) -> str:
        return f"{self.value[0],self.value[1]}"
    
    @property
    def width(self) -> int:
        return self.value[0]

    @property
    def height(self) -> int:
        return self.value[1]