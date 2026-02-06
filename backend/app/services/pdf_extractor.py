import PyPDF2
import pdfplumber
from typing import Dict, List, Optional
import re

class PDFExtractor:
    """Service pour extraire le texte et les données des PDFs"""
    
    @staticmethod
    def extract_text_pypdf2(file_path: str) -> str:
        """Extraire le texte avec PyPDF2"""
        try:
            text = ""
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
            return text
        except Exception as e:
            print(f"❌ Erreur PyPDF2: {e}")
            return ""
    
    @staticmethod
    def extract_text_pdfplumber(file_path: str) -> str:
        """Extraire le texte avec pdfplumber (meilleure qualité)"""
        try:
            text = ""
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            return text
        except Exception as e:
            print(f"❌ Erreur pdfplumber: {e}")
            return ""
    
    @staticmethod
    def extract_text(file_path: str) -> str:
        """Extraire le texte (essaie plusieurs méthodes)"""
        print(f"🔵 Extraction du texte de: {file_path}")
        
        # Essayer pdfplumber d'abord (meilleure qualité)
        text = PDFExtractor.extract_text_pdfplumber(file_path)
        
        # Si échec, essayer PyPDF2
        if not text or len(text) < 50:
            text = PDFExtractor.extract_text_pypdf2(file_path)
        
        print(f"✅ Texte extrait: {len(text)} caractères")
        return text
    
    @staticmethod
    def extract_tables(file_path: str) -> List[List[str]]:
        """Extraire les tableaux du PDF"""
        try:
            tables = []
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_tables = page.extract_tables()
                    if page_tables:
                        tables.extend(page_tables)
            print(f"✅ {len(tables)} tableau(x) extrait(s)")
            return tables
        except Exception as e:
            print(f"❌ Erreur extraction tableaux: {e}")
            return []
