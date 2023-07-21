from shop.helper.const import quit_word
from shop.dictionary.products import ShoppingList
from shop.utils.funcs import ShoppingListApp
from shop.dictionary.products import NamePasswords

def main():

    while True:
        name, password = ShoppingListApp.get_name_password()

        if ShoppingListApp.name_password_exists(name, password):
            print("You logged in!")

            item = input("Enter something: ").lower()

            if item in quit_word:
                ShoppingListApp.spell_shop(ShoppingList.shop_item)
                print(len(ShoppingList.shop_item))
                break
            elif item == "help":
                ShoppingListApp.help()
            elif item == "search":
                shop_item = input("What do you want to search?")
                ShoppingListApp.search_shop(ShoppingList.shop_item, shop_item)
            elif item == "change":
                shop = input("Which product do you want to move?")
                shop_change = input("Which product do you want to replace it with?")
                ShoppingListApp.first_show(ShoppingList.shop_item, shop, shop_change)
                print(f"This {shop} changed to this {shop_change}")
            elif item == "check":
                shop_type = input("What do you want to do? ")
                shop_item = input("Do you want to make any changes? ")
                ShoppingListApp.check_shop(ShoppingList.shop_item, shop_type, shop_item)
            elif item not in quit_word and item in ShoppingList.shop_item:
                ShoppingListApp.add_to_list(item)
        else:
            print("Your username or password is incorrect. \n you can singe in")
            