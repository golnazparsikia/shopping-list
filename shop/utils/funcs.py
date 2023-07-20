from shop.dictionary.products import ShoppingList
from shop.helper.const import quit_word

class ShoppingListApp:

    @staticmethod
    def spell_shop(final_list: list):
        for word in final_list:
            print(word)

    @staticmethod
    def help():
        print("(quit, exit, ex, q) throws you out of the loop")
        print("If you insert 'check', you can remove, read, or confirm your list")

    @staticmethod
    def plus_shop():
        plus_list = []
        for shop in ShoppingList.shopping:
            if shop in ShoppingList.shop_item:
                plus = ShoppingList.shop_item[shop][0]
                plus_list.append(plus)
        return sum(plus_list)

    @classmethod
    def add_to_list(cls, shop: str):
        try:
            num = int(input("How many do you want? "))
        except:
            print("it is not a number!")
        if shop in ShoppingList.shop_item:
            if ShoppingList.shop_item[shop][1] >= num and ShoppingList.shop_item[shop][1] >= 1:
                ShoppingList.shop_item[shop][1] -= num
                for i in range(num):
                    ShoppingList.shopping.append(shop)
                print(ShoppingList.shop_item[shop])
                print(f"{num} {shop} added to the shopping list, total items: {len(ShoppingList.shopping)}")
                print(f"The total price of your shopping: {cls.plus_shop()}")
            elif ShoppingList.shop_item[shop][1] <= 0:
                print("this item finished!")
            elif ShoppingList.shop_item[shop][1] <= num:
                print("this number is not available!")
            
            else:
                print("Item finished!")


    @classmethod
    def search_shop(cls, shop_list, shop):
        if shop in shop_list:
            print('YES')
        else:
            print('NO')

    @classmethod
    def check_shop(cls, shop_list, shop_default, shop):
        if shop_default == "remove":
            shop_list.remove(shop)
        elif shop_default == "read":
            print(shop_list)
        elif shop_default == "confirm":
            cls.spell_shop(final_list=shop_list)
        else:
            print("Invalid command!")

    @classmethod
    def first_show(cls, shop_list, shop, shop_change):
        if shop in shop_list and shop_change in shop_list:
            shop_num = shop_list.index(shop)
            shop_change_num = shop_list.index(shop_change)
            shop_list[shop_num] = shop_change
            shop_list[shop_change_num] = shop
        else:
            print("Invalid product names!")
