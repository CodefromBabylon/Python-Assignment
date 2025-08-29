# Assignment 1: Smartphone Class with Inheritance and Polymorphism

class SmartDevice:
    """Parent class for all smart devices"""
    
    def __init__(self, brand, model, operating_system, battery_level=100):
        self.brand = brand
        self.model = model
        self.operating_system = operating_system
        self._battery_level = battery_level  # Encapsulated attribute
        self.is_powered_on = False
    
    def power_on(self):
        """Power on the device"""
        if self._battery_level > 5:
            self.is_powered_on = True
            return f"{self.brand} {self.model} is now powered on! 📱"
        return "Battery too low to power on! ⚡"
    
    def power_off(self):
        """Power off the device"""
        self.is_powered_on = False
        return f"{self.brand} {self.model} is now powered off. 💤"
    
    def check_battery(self):
        """Check battery level (encapsulated access)"""
        return f"Battery level: {self._battery_level}%"
    
    def charge(self, amount):
        """Charge the device"""
        if amount > 0:
            self._battery_level = min(100, self._battery_level + amount)
            return f"Charging... Now at {self._battery_level}% 🔌"
        return "Invalid charging amount!"
    
    def use_battery(self, amount):
        """Use battery (protected method)"""
        if self.is_powered_on:
            self._battery_level = max(0, self._battery_level - amount)
            return self._battery_level > 0
    
    def perform_action(self):
        """Polymorphic method - to be overridden by child classes"""
        return "Performing generic smart device action..."

class Smartphone(SmartDevice):
    """Child class representing a smartphone"""
    
    def __init__(self, brand, model, operating_system, storage_gb, ram_gb, 
                 camera_mp, battery_level=100):
        super().__init__(brand, model, operating_system, battery_level)
        self.storage_gb = storage_gb
        self.ram_gb = ram_gb
        self.camera_mp = camera_mp
        self._screen_brightness = 50  # Private attribute
        self.apps_installed = []
    
    def make_call(self, number):
        """Make a phone call"""
        if self.use_battery(2):
            return f"📞 Calling {number}..."
        return "Battery too low to make call! ⚡"
    
    def send_message(self, number, message):
        """Send a text message"""
        if self.use_battery(1):
            return f"✉️ Sent to {number}: {message}"
        return "Battery too low to send message! ⚡"
    
    def take_photo(self):
        """Take a photo using the camera"""
        if self.use_battery(3):
            return f"📸 Photo taken with {self.camera_mp}MP camera!"
        return "Battery too low to take photo! ⚡"
    
    def install_app(self, app_name):
        """Install a new app"""
        if len(self.apps_installed) < self.storage_gb // 2:  # Simple storage check
            self.apps_installed.append(app_name)
            self.use_battery(1)
            return f"⬇️ Installed {app_name}"
        return "Not enough storage to install app! 💾"
    
    def set_brightness(self, level):
        """Set screen brightness (encapsulation example)"""
        if 0 <= level <= 100:
            self._screen_brightness = level
            return f"Brightness set to {level}%"
        return "Invalid brightness level!"
    
    def get_brightness(self):
        """Get screen brightness (controlled access)"""
        return f"Screen brightness: {self._screen_brightness}%"
    
    def perform_action(self):
        """Override parent method - polymorphism in action"""
        return "📱 Smartphone is making a call and taking photos!"

class GamingPhone(Smartphone):
    """Specialized smartphone for gaming"""
    
    def __init__(self, brand, model, operating_system, storage_gb, ram_gb, 
                 camera_mp, gpu_model, refresh_rate_hz, battery_level=100):
        super().__init__(brand, model, operating_system, storage_gb, ram_gb, 
                        camera_mp, battery_level)
        self.gpu_model = gpu_model
        self.refresh_rate_hz = refresh_rate_hz
        self._game_mode = False
    
    def enable_game_mode(self):
        """Enable special gaming mode"""
        self._game_mode = True
        self._screen_brightness = 100
        return "🎮 Game mode enabled! Maximum performance activated!"
    
    def disable_game_mode(self):
        """Disable gaming mode"""
        self._game_mode = False
        self._screen_brightness = 50
        return "Game mode disabled."
    
    def play_game(self, game_name):
        """Play a game with enhanced performance"""
        if self._game_mode:
            battery_used = 5
        else:
            battery_used = 8
        
        if self.use_battery(battery_used):
            return f"🎯 Playing {game_name} at {self.refresh_rate_hz}Hz refresh rate!"
        return "Battery too low to play game! ⚡"
    
    def perform_action(self):
        """Override parent method - polymorphism"""
        return "🎮 Gaming phone is running high-performance games!"

# Activity 2: Polymorphism Challenge
def demonstrate_polymorphism(devices):
    """Demonstrate polymorphism by calling perform_action on different devices"""
    print("\n" + "="*50)
    print("POLYMORPHISM DEMONSTRATION:")
    print("="*50)
    
    for device in devices:
        print(f"{device.brand} {device.model}: {device.perform_action()}")

# Main program
if __name__ == "__main__":
    print("=== SMART DEVICE SHOWCASE ===")
    
    # Create different smartphone objects
    iphone = Smartphone("Apple", "iPhone 15", "iOS", 256, 8, 48, 95)
    samsung = Smartphone("Samsung", "Galaxy S23", "Android", 512, 12, 200, 85)
    gaming_phone = GamingPhone("ASUS", "ROG Phone 7", "Android", 1024, 16, 
                             50, "Adreno 740", 165, 90)
    
    # Demonstrate smartphone features
    print(iphone.power_on())
    print(iphone.make_call("555-1234"))
    print(iphone.take_photo())
    print(iphone.install_app("Instagram"))
    print(iphone.check_battery())
    print()
    
    print(samsung.power_on())
    print(samsung.send_message("555-5678", "Hello there!"))
    print(samsung.set_brightness(75))
    print(samsung.get_brightness())
    print()
    
    print(gaming_phone.power_on())
    print(gaming_phone.enable_game_mode())
    print(gaming_phone.play_game("Call of Duty Mobile"))
    print(gaming_phone.install_app("PUBG Mobile"))
    print(gaming_phone.check_battery())
    
    # Demonstrate polymorphism
    devices = [iphone, samsung, gaming_phone]
    demonstrate_polymorphism(devices)
    
    # Show inheritance hierarchy
    print("\n" + "="*50)
    print("INHERITANCE HIERARCHY:")
    print("="*50)
    print("SmartDevice (Grandparent)")
    print("└── Smartphone (Parent)")
    print("    └── GamingPhone (Child)")