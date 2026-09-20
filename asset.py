class Asset:
    asset_id_counter = 0
    def __init__(self, user_id, asset_type, name, value):
        self.user_id = user_id
        self.asset_type = asset_type 
        self.name = name
        self.value = value
        Asset.asset_id_counter += 1
        self.asset_id = Asset.asset_id_counter

    def display_asset_details(self):
        print("===ASSET DETAILS===")
        print(f"ASSET ID (auto-generated): {self.asset_id}")
        print(f"ASSET TYPE: {self.asset_type}")
        print(f"NAME: {self.name}")
        print(f"VALUE: {self.asset_value}")
