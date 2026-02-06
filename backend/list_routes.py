"""Lister toutes les routes disponibles dans l'API"""
from app.main import app

print("\n📋 ROUTES DISPONIBLES DANS L'API:\n")
print("=" * 80)

for route in app.routes:
    if hasattr(route, 'methods') and hasattr(route, 'path'):
        methods = ', '.join(route.methods)
        print(f"{methods:20} {route.path}")

print("=" * 80)
print("\nRecherche de routes avec 'documents':")
for route in app.routes:
    if hasattr(route, 'path') and 'document' in route.path.lower():
        methods = ', '.join(route.methods) if hasattr(route, 'methods') else 'N/A'
        print(f"  ✓ {methods:20} {route.path}")
