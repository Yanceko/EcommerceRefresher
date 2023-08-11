from flask import Flask, render_template
#flask --app app.py --debug run

app = Flask(__name__)

@app.route("/")
def home():
    team_name = "Algorithm Alchemists"
    your_name = "Chadric Nathan"
    profile_photo = "profile.jpeg" 
    return render_template("homepage.html", team_name=team_name, your_name=your_name, profile_photo=profile_photo)

# Sample product data
products = [
    {
        'id': 1,
        'title': 'IPAD',
        'price': 599.99,
        'image': 'product1.jpg',
        'description':'The iPad is a touchscreen tablet PC made by Apple. '
    },
    {
        'id': 2,
        'title': 'Iphone',
        'price': 899.99,
        'image': 'product2.jpg',
        'description': 'The iPhone is a smartphone made by Apple that combines a computer, iPod, digital camera and cellular phone into one device with a touchscreen interface.'
    },
    {
        'id': 3,
        'title': 'MACLaptop',
        'price': 1199.99,
        'image': 'product3.jpg',
        'description': 'A family of desktop and laptop computers from Apple,'
    },
    {
        'id': 4,
        'title': 'Galaxy Phone',
        'price': 999.99,
        'image': 'product4.jpg',
        'description': 'Samsung Galaxy is Samsung Electronics flagship line of Android smartphones and tablets.'
    },
    
]

@app.route("/products")
def product_list():
    return render_template("products.html", products=products)

@app.route("/products/<int:product_id>")
def product_details(product_id):
    
    selected_product = None
    for product in products:
        if product['id'] == product_id:
            selected_product = product
            break

    if selected_product:
        return render_template("product_details.html", product=selected_product)
    else:
        return "Product not found"


if __name__ == "__main__":
    app.run(debug=True)
