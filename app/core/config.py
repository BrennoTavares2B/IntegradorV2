from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    WC_BASE_URL: str = os.getenv("WC_BASE_URL", "")
    WC_KEY: str = os.getenv("WC_KEY", "")
    WC_SECRET: str = os.getenv("WC_SECRET", "")
    DB_URL: str = os.getenv("DB_URL", "")
    
    def validate(self) -> None:
        """Valida se todas as configurações necessárias estão definidas"""
        missing = []
        if not self.WC_BASE_URL:
            missing.append("WC_BASE_URL")
        if not self.WC_KEY:
            missing.append("WC_KEY")
        if not self.WC_SECRET:
            missing.append("WC_SECRET")
        if not self.DB_URL:
            missing.append("DB_URL")
        
        if missing:
            raise ValueError(f"Variáveis de ambiente faltando: {', '.join(missing)}")

settings = Settings()

