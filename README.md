# Django-shopping-app

APIs for Products:
1. Add a product:[POST] http://127.0.0.1:8000/product/
         mock-request: {
          "name": "Product 1",
          "description": "This is the first product",
          "price": 150

        }
        
2. Fetch All product: [GET] http://127.0.0.1:8000/product/get-products



APIs for Orders:
1. Create an order: [POST] http://127.0.0.1:8000/order/
        mock-request: {
            "product": 3,
            "quantity": 3
        }
  
2. Fetch All orders: [GET] http://127.0.0.1:8000/order/get-orders


3. Fetch All order after a particular date: [GET] http://127.0.0.1:8000/order/get-orders-intervals
        mock-request: {
            "date": "2022-06-25"
        }
