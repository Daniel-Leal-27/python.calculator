from flask import Flask, render_template, request
app=Flask(__name__, template_folder="./views")

@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method=="GET"):
        return render_template("index.html")
    else: 
        if (request.form["num1"] != "" and request.form["num2"] != ""  ):
            num1 = request.form["num1"]
            num2 = request.form["num2"]
            opc = request.form["opc"]

            if (opc == "soma"):
                soma = int(num1) + int(num2)
                return str(soma)
            elif (opc == "subt"):
                subt = int(num1) - int(num2)
                return str(subt)
            elif (opc == "multi"):
                multi = int(num1) * int(num2)
                return str(multi)
            else:
                div = int(num1) / int(num2)
                return str(div)
                
        else:
            return "Preencha todo o formulário"

app.run(port = 8000, debug=True)


#SERVIDOR HTTP CONFIGURADO
#render_template mostra o html
#request serve para ciar parâmetros via URL, paracido com Body-parser
#Flask é igual do Express do Node
#Porta padrão Python é 5000