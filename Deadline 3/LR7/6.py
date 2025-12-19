class DatabaseConfig:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.db_name = args[0] if args else None
            cls._instance.user = args[1] if len(args) > 1 else None
            cls._instance.password = args[2] if len(args) > 2 else None
        return cls._instance


if __name__ == "__main__":
    conf1 = DatabaseConfig("shop_db", "admin", "123")
    conf2 = DatabaseConfig("users_db", "root", "000")
    
    print(conf1 is conf2)
    print(f"conf1: {conf1.db_name}, {conf1.user}, {conf1.password}")
    print(f"conf2: {conf2.db_name}, {conf2.user}, {conf2.password}")