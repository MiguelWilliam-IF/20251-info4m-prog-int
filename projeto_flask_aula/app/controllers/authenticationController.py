from flask import render_template, flash

class AuthenticationController:
    
    def login(form):
        password = form.password.data
        
        flash(f"O usuario {form.username.data} fez o login, lembrar={form.remember_me.data}")
        usuario_logado = {
            'nome': form.username.data
        }
        return render_template("index.html", usuario = usuario_logado, usuario_logado = True)