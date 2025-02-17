class Cart():
    
    def __init__(self, request):
        
        self.session = request.session      # Returning user obtain existing session
        
        cart = self.session.get('session_key')
        
        # New visitor generate session key
        
        if 'session_key' not in request.session: 
        
            cart = self.session['session_key']= {}
            
        # Remember it user has product in cart
        self.cart = cart
        
    def add(self, product, product_qty):
        
        product_id = str(product_id)
        
        if product_id in self.cart:
            
            self.cart[product_id] ['qty'] = product_qty
            
        else: 
            
            self.cart[product_id]={'price': str(product.price),'qty':product_qty}
            
            self.session.modified = True