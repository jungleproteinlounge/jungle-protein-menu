from django.core.management.base import BaseCommand
from menu.models import Category, Product

DATA = [
("Malteadas de proteína", [
("Malteada de proteína — 16 oz con agua", 21900, "Elige tu sabor favorito."),
("Malteada de proteína — 16 oz con leche", 23900, "Elige tu sabor favorito."),
("Malteada de proteína — 22 oz con agua", 23900, "Elige tu sabor favorito."),
("Malteada de proteína — 22 oz con leche", 25900, "Elige tu sabor favorito."),
("Sabores disponibles", None, "Arándanos, pie de limón, pan de banano, fresa salvaje, chocolate, Oreo, Maní Maní, mocca, canela roll, vainilla, alfajor, almendras y sabor de temporada. Verificar contra la carta final."),
("Salsas y toppings", None, "Salsas: arequipe, arequipe sin azúcar y chocolate. Toppings: maní, almendras trituradas, mantequilla de maní, crocante de proteína, minichips, chips de chocolate, Oreo triturada, chantilly y galletas de limón."),
]),
("Extras", [
("Guaraná", 3000, ""), ("Proteína", 5500, ""), ("Aloe", 3000, ""),
("Té Quemador", 4500, ""), ("Fibra", 6000, ""), ("BetaHeart", 5000, ""),
]),
("Bebidas funcionales", [
("Frutos Rojos", 18500, ""), ("Golden Mix", 18500, ""), ("Colágeno Hidrolizado", 18500, ""),
("Pre-entreno", 18500, ""), ("Chupapanza", 18000, ""), ("Electrolitos CR7", 16500, ""),
]),
("Waffles y antojos", [
("WaffleBono", 22900, ""), ("WaffleSandwich", 25900, ""), ("Trufas", 8000, ""), ("Galletas proteicas", 9000, ""),
]),
("Bebidas calientes", [
("Coffee Extra", 19000, ""), ("Café Caramelo", 19000, ""), ("Chai", 19000, ""),
("Chupapanza", 18000, ""), ("Café Amaretto", 19000, ""),
]),
("Cafés proteicos", [
("Caramelo Amaretto Coffee", 22000, ""), ("Extra Protein Iced Chai", 22000, ""),
]),
("Recuperación muscular", [
("Malteada de recuperación muscular", 25000, "Precio leído en la carta; confirmar antes de publicar."),
]),
("Programas", [
("Detox 10 días", 165000, ""), ("Plan Comprométete", 260000, ""), ("Recomposición corporal", 495000, ""),
]),
]
class Command(BaseCommand):
    help = "Carga los productos y precios iniciales de Jungle Protein Lounge."
    def handle(self, *args, **options):
        for cat_order, (cat_name, products) in enumerate(DATA, 1):
            category, _ = Category.objects.get_or_create(name=cat_name, defaults={"sort_order": cat_order})
            category.sort_order = cat_order
            category.save()
            for prod_order, (name, price, description) in enumerate(products, 1):
                Product.objects.update_or_create(
                    category=category, name=name,
                    defaults={"price_cop": price, "description": description, "sort_order": prod_order, "active": True}
                )
        self.stdout.write(self.style.SUCCESS("Menú inicial cargado. Revisa productos y precios antes de publicar."))
