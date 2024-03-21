from flask import Flask, render_template, request
import funcoes_auxiliares as fa
import busca_sem_pesos_FATEC as bs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    # Carrega o mapa do arquivo
    mapa = fa.Gera_Problema_Grade("mapa.txt")
    dim_x = len(mapa)
    dim_y = len(mapa[0])

    # Obtém os dados do formulário
    origem_x = int(request.form['origem_x'])
    origem_y = int(request.form['origem_y'])
    destino_x = int(request.form['destino_x'])
    destino_y = int(request.form['destino_y'])
    
    # Verifica o tipo de busca selecionado
    tipo_busca = request.form['tipo_busca']

    # Executa o algoritmo de busca correspondente
    sol = bs.busca()
    if tipo_busca == 'amplitude':
        caminho_amplitude = sol.amplitude([origem_x, origem_y], [destino_x, destino_y], mapa, dim_x, dim_y)
        caminho_profundidade = None  # Define como None para não mostrar na página
        print("\n===> AMPLITUDE:", caminho_amplitude)
        print("===> Custo do Caminho:", len(caminho_amplitude) - 1) 
    elif tipo_busca == 'profundidade':
        caminho_amplitude = None  # Define como None para não mostrar na página
        caminho_profundidade = sol.profundidade([origem_x, origem_y], [destino_x, destino_y], mapa, dim_x, dim_y)
        print("\n*****PROFUNDIDADE*****\n", caminho_profundidade)    
        print("===> Custo do Caminho:", len(caminho_profundidade) - 1)
    # Renderiza o resultado na página
    return render_template('resultado.html', caminho_amplitude=caminho_amplitude, caminho_profundidade=caminho_profundidade)

if __name__ == '__main__':
    app.run(debug=False)




