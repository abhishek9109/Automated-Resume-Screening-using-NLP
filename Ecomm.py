

class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
        else:
            raise ValueError("Insufficient stock")

    def __str__(self):
        return f"{self.name} - ${self.price} (Stock: {self.stock})"


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.id in self.items:
            self.items[product.id]['quantity'] += quantity
        else:
            self.items[product.id] = {'product': product, 'quantity': quantity}

    def remove_product(self, product_id):
        if product_id in self.items:
            del self.items[product_id]

    def view_cart(self):
        return {item['product'].name: {'quantity': item['quantity'], 'price': item['product'].price}
                for item in self.items.values()}

    def total_amount(self):
        return sum(item['quantity'] * item['price'] for item in self.view_cart().values())


class Order:
    def __init__(self, cart):
        self.cart = cart
        self.total_amount = cart.total_amount()

    def __str__(self):
        return f"Order Total: ${self.total_amount}"


class User:
    def __init__(self, username):
        self.username = username
        self.cart = Cart()

    def add_to_cart(self, product, quantity):
        self.cart.add_product(product, quantity)

    def checkout(self):
        order = Order(self.cart)
        return order


class Admin:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.id] = product

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def update_product(self, product_id, name=None, price=None, stock=None):
        if product_id in self.products:
            product = self.products[product_id]
            if name is not None:
                product.name = name
            if price is not None:
                product.price = price
            if stock is not None:
                product.stock = stock

    def view_products(self):
        return {product.name: {'price': product.price, 'stock': product.stock}
                for product in self.products.values()}


# Example usage
if __name__ == "__main__":
    # Create some products
    p1 = Product(1, "Laptop", 1000, 10)
    p2 = Product(2, "Smartphone", 500, 20)
    
    # Admin adds products
    admin = Admin()
    admin.add_product(p1)
    admin.add_product(p2)
    
    # User interaction
    user = User("john_doe")
    print("Available products:")
    print(admin.view_products())
    
    # User adds products to cart
    user.add_to_cart(p1, 1)
    user.add_to_cart(p2, 2)
    
    # User checks out
    order = user.checkout()
    print("Cart contents:")
    print(user.cart.view_cart())
    print(order)
    
    # Admin updates product details
    admin.update_product(1, price=950, stock=8)
    print("Updated product list:")
    print(admin.view_products())




यह Python कोड एक सरल शॉपिंग सिस्टम को दर्शाता है जिसमें विभिन्न क्लासेज़ (classes) बनाई गई हैं। इसमें Product, Cart, Order, User, और Admin जैसी क्लासेज़ का उपयोग किया गया है। आइए इसे हिंदी में समझते हैं:

1. Product Class (उत्पाद वर्ग):
Product एक उत्पाद को दर्शाता है, जैसे लैपटॉप, स्मार्टफोन आदि।
इसके अंदर चार विशेषताएँ होती हैं: id (उत्पाद की पहचान), name (नाम), price (मूल्य), और stock (मौजूद स्टॉक)।
update_stock मेथड स्टॉक में से मात्रा घटाने के लिए उपयोग किया जाता है। अगर स्टॉक पर्याप्त नहीं है, तो यह एक त्रुटि (error) देगा।
__str__ मेथड का उपयोग उत्पाद का विवरण (जैसे नाम, मूल्य, और स्टॉक) को प्रिंट करने के लिए होता है।
2. Cart Class (कार्ट वर्ग):
Cart वह जगह है जहाँ उपयोगकर्ता अपने उत्पादों को जोड़ते हैं।
इसमें items नाम की एक dictionary होती है जो उत्पाद और उसकी मात्रा को स्टोर करती है।
add_product मेथड किसी उत्पाद को कार्ट में जोड़ने के लिए है। यदि उत्पाद पहले से कार्ट में है, तो यह उसकी मात्रा बढ़ा देगा।
remove_product किसी उत्पाद को कार्ट से हटाने के लिए है।
view_cart मेथड कार्ट में रखे गए सभी उत्पादों और उनकी जानकारी को दिखाता है।
total_amount मेथड पूरे कार्ट का कुल मूल्य बताता है।
3. Order Class (ऑर्डर वर्ग):
Order वह क्लास है जो किसी ऑर्डर को दर्शाती है। इसमें कार्ट से जुड़ी सभी जानकारी होती है।
__str__ मेथड ऑर्डर का कुल मूल्य प्रिंट करता है।
4. User Class (उपयोगकर्ता वर्ग):
User एक उपयोगकर्ता को दर्शाता है।
इसमें एक cart होता है जो उपयोगकर्ता के द्वारा चुने गए उत्पादों को रखता है।
add_to_cart मेथड किसी उत्पाद को उपयोगकर्ता के कार्ट में जोड़ने के लिए है।
checkout मेथड कार्ट को ऑर्डर में बदलता है और ऑर्डर का कुल मूल्य प्रिंट करता है।
5. Admin Class (प्रशासक वर्ग):
Admin वह क्लास है जो उत्पादों को प्रबंधित करता है।
इसमें एक dictionary होती है, जिसमें सभी उत्पादों की जानकारी होती है।
add_product मेथड किसी उत्पाद को सिस्टम में जोड़ने के लिए है।
remove_product मेथड किसी उत्पाद को सिस्टम से हटाने के लिए है।
update_product मेथड किसी उत्पाद के नाम, मूल्य, या स्टॉक को अपडेट करने के लिए है।
view_products मेथड सभी उत्पादों की सूची और उनकी जानकारी दिखाता है।
Example (उदाहरण):
Admin दो उत्पाद (लैपटॉप और स्मार्टफोन) सिस्टम में जोड़ता है।
User (जॉन डो) इन उत्पादों को कार्ट में डालता है।
फिर, User चेकआउट करता है और ऑर्डर की जानकारी प्राप्त करता है।
इसके बाद, Admin उत्पादों के मूल्य और स्टॉक को अपडेट करता है।
यह कोड एक शॉपिंग सिस्टम के रूप में काम करता है जहाँ एडमिन उत्पादों को जोड़ और अपडेट कर सकता है, और उपयोगकर्ता उत्पादों को कार्ट में डालकर ऑर्डर कर सकता है।







You said:
explain
ChatGPT said:
ChatGPT
इस कोड में एक सरल शॉपिंग सिस्टम बनाया गया है जिसमें विभिन्न क्लासेज़ (classes) का उपयोग करके उत्पादों को प्रबंधित (manage) किया जा सकता है, कार्ट में जोड़ा जा सकता है, और ऑर्डर किया जा सकता है। इसका उद्देश्य एक ऑनलाइन शॉपिंग प्लेटफ़ॉर्म के बुनियादी कार्यों को प्रदर्शित करना है। आइए इसको सरल भाषा में समझते हैं:

1. Product Class (उत्पाद क्लास):
Product वह क्लास है जो किसी उत्पाद (जैसे लैपटॉप या स्मार्टफोन) का प्रतिनिधित्व करती है।
जब हम इस क्लास से कोई उत्पाद बनाते हैं, तो हम उसे एक id, name (नाम), price (कीमत), और stock (स्टॉक) देते हैं।
उदाहरण के लिए: p1 = Product(1, "Laptop", 1000, 10) - यह एक लैपटॉप है जिसकी कीमत 1000 है और 10 यूनिट स्टॉक में हैं।
update_stock मेथड से उत्पाद का स्टॉक कम किया जा सकता है। उदाहरण के लिए, अगर कोई उत्पाद खरीदता है तो उसकी स्टॉक में से उस मात्रा को घटा दिया जाता है।
__str__ मेथड का उपयोग प्रिंट करने के लिए होता है ताकि हम देख सकें कि उत्पाद का नाम, कीमत, और स्टॉक कितना है।
2. Cart Class (कार्ट क्लास):
Cart क्लास एक शॉपिंग कार्ट को दर्शाती है जिसमें उपयोगकर्ता अपने चुने हुए उत्पादों को जोड़ सकता है।
इसमें एक dictionary होती है जिसमें product id के अनुसार उत्पाद और उसकी मात्रा (quantity) स्टोर होती है।
add_product मेथड का उपयोग कार्ट में उत्पाद जोड़ने के लिए किया जाता है। अगर वही उत्पाद पहले से है, तो उसकी मात्रा बढ़ा दी जाती है।
remove_product मेथड किसी उत्पाद को कार्ट से हटाने के लिए है।
view_cart मेथड से आप कार्ट में क्या-क्या जोड़ा गया है, यह देख सकते हैं।
total_amount मेथड से पूरे कार्ट का कुल मूल्य निकाल सकते हैं।
3. Order Class (ऑर्डर क्लास):
Order क्लास से उपयोगकर्ता का कार्ट चेकआउट के बाद एक ऑर्डर में बदल जाता है।
इसका काम यह है कि जब कोई उपयोगकर्ता कार्ट से ऑर्डर करता है, तो वह ऑर्डर का कुल मूल्य (total amount) बताता है।
__str__ मेथड से ऑर्डर का विवरण प्रिंट होता है, जैसे कि "Order Total: $2300"।
4. User Class (उपयोगकर्ता क्लास):
User क्लास किसी उपयोगकर्ता को दर्शाती है। इसमें उपयोगकर्ता का नाम और उसका कार्ट होता है।
उपयोगकर्ता add_to_cart मेथड से उत्पादों को अपने कार्ट में जोड़ सकता है।
checkout मेथड उपयोगकर्ता के कार्ट को ऑर्डर में बदल देता है और कुल मूल्य को बताता है।
5. Admin Class (प्रशासक क्लास):
Admin क्लास सिस्टम के व्यवस्थापक (admin) को दर्शाती है, जो उत्पादों को जोड़ने, हटाने और अपडेट करने का काम करता है।
add_product मेथड से एडमिन नए उत्पाद जोड़ सकता है।
remove_product मेथड से एडमिन किसी उत्पाद को सिस्टम से हटा सकता है।
update_product मेथड से एडमिन किसी उत्पाद का नाम, कीमत, या स्टॉक बदल सकता है।
view_products मेथड से एडमिन सभी उपलब्ध उत्पादों की सूची और उनकी जानकारी देख सकता है।
Example (उदाहरण):
Admin ने दो उत्पाद जोड़े: Laptop और Smartphone।
User (जॉन डो) ने इन उत्पादों को अपने कार्ट में डाला: 1 लैपटॉप और 2 स्मार्टफोन।
फिर User ने चेकआउट किया और ऑर्डर का कुल मूल्य देखा।
इसके बाद, Admin ने उत्पादों की कीमत और स्टॉक को अपडेट किया।
इस तरह, यह एक शॉपिंग प्लेटफ़ॉर्म की तरह काम करता है जहाँ उत्पाद को देखा, कार्ट में जोड़ा, और ऑर्डर किया जा सकता है, और एडमिन उत्पादों को प्रबंधित कर सकता है।









