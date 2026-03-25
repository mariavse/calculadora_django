from django.shortcuts import render

def calculadora(request):
    resultado = None
    if request.method == "POST":
        n1 = float(request.POST.get('n1', 0))
        n2 = float(request.POST.get('n2', 0))
        op = request.POST.get('op')
        
        # O curl ou o navegador podem enviar o '+' como um espaço ' '
        if op == '+' or op == ' ': resultado = n1 + n2
        elif op == '-': resultado = n1 - n2
        elif op == '*': resultado = n1 * n2
        elif op == '/': resultado = n1 / n2 if n2 != 0 else "Erro"
            
    return render(request, "index.html", {"resultado": resultado})