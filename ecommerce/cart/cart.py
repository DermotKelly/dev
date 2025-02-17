class Cart():
    
    def __init__(self, request):
        
        self.session = request.session      # Returning user obtain existing session
        
        cart = self.session.get('session_key')
        
        # New visitor generate session key
        
        if 'session_key' not in request.session: 
        
            cart = self.session['session_key']= {}
            
        # Remember it user has product in cart
        self.cart = cart