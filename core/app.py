from shop.helper.const import quit_word
from shop.dictionary.products import ShoppingList
from shop.utils.funcs import ShoppingListApp


def main():
    while True:
        item = input("Enter something: ")
        item = item.lower()
    
        if item in quit_word :
            ShoppingListApp.spell_shop(ShoppingList.shopping)
            print(len(ShoppingList.shopping))
            break
        elif item == "help":
            ShoppingListApp.help()
        elif item == "search":
            shop_item = input("what do you want to search?")
            ShoppingListApp.search_shop(ShoppingList.shopping, shop_item)
        elif item == "change":
            shop = input("Which product do you want to move?")
            shop_change = input("Which product do you want to replace it with?")
            ShoppingListApp.first_show(ShoppingList.shopping, shop, shop_change)
            print(f"this {shop} changed to this {shop_change}")
        elif item == "check":
            shop_type = input("what do you want to do? ")
            shop_item = input("Do you want to make any changes? ")
            ShoppingListApp.check_shop(ShoppingList.shopping, shop_type, shop_item)
        elif item not in quit_word and item in ShoppingList.shop_item:
            ShoppingListApp.add_to_list(item)