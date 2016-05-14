from system.core.controller import *
class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')
    def index(self):
        return self.load_view('index.html')
    def register(self):
        user_info = self.models['WelcomeModel'].register(request.form)
        if user_info['status'] == True:
            session['id'] = user_info['user']['id'] 
            session['name'] = user_info['user']['first_name']            
            return self.load_view('success.html')
        else:
            for message in user_info['errors']:
                flash(message)
            return redirect('/')
    def login(self):
        login_info = self.models['WelcomeModel'].login(request.form)
        print login_info
        if login_info['status'] == True:
            session['id'] = login_info['user']['id'] 
            session['name'] = login_info['user']['first_name']
            return self.load_view('success.html')
        else:
            for message in login_info['errors']:
                flash(message)
            return redirect('/')