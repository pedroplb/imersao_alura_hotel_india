import pandas as pd
import api
import matplotlib.pyplot as plt

def limpa_dados():
    # esta funçao tem como objetivo importar os dados da pesquisa e tratar os dados numéricos

    dados = pd.read_csv('base/munnar.csv')
    dados['Price'] = dados['Price'].str.replace(',', '')
    dados['Price'] = pd.to_numeric(dados['Price'])
    dados['Tax'] = dados['Tax'].str.replace(',', '')
    dados['Tax'] = pd.to_numeric(dados['Tax'])

    return dados


def calcula_preco_total_real(dados_tratados):
    # esta funçao tem como objetivo calcular o preço total em reais de cada hotel

    dados_tratados['preco_total'] = dados_tratados['Price'] + dados_tratados['Tax']
    cambio = api.buscar_taxa_cambio('INR', 'BRL')
    dados_tratados['preco_total_R$'] = round(dados_tratados['preco_total'] * cambio, 2)

    return dados_tratados


def calcula_esforco(dados_tratados):
    # esta funçao tem como objetivo saber quantas horas de trabalho são necessárias para
    # cada diária baseado no salário mínimo mensal de 1320 reais, 21 dias úteis e 8h dia

    dados_tratados['hr_trabalho'] = dados_tratados["preco_total_R$"] / (1320 / 21 / 8)

    return dados_tratados

def visualiza_preco_vs_rating(dados_preco_esforco):

    # Calcula a média de preço por classificação
    media_preco_por_classificacao = dados_preco_esforco.groupby('Star Rating')['preco_total_R$'].mean()

    # Cria um gráfico de barras da média de preço por classificação
    plt.bar(media_preco_por_classificacao.index, media_preco_por_classificacao.values)
    plt.xlabel('Classificação')
    plt.ylabel('Média de Preço')
    plt.title('Média de Preço (R$) por Classificação')
    plt.xticks(media_preco_por_classificacao.index)

    # Adiciona os valores da média nas barras
    for i, v in enumerate(media_preco_por_classificacao.values):
        plt.text(i + 2, v, f'{v:.2f}', ha='center', va='bottom')

    plt.show()

def visualiza_esforco_vs_rating(dados_preco_esforco):

    # Calcula a média de preço por classificação
    media_preco_por_classificacao = dados_preco_esforco.groupby('Star Rating')['hr_trabalho'].mean()

    # Cria um gráfico de barras da média de preço por classificação
    plt.bar(media_preco_por_classificacao.index, media_preco_por_classificacao.values)
    plt.xlabel('Classificação')
    plt.ylabel('Média de Horas de Trabalho')
    plt.title('Média de Horas de Trabalho Necessárias por Classificação')
    plt.xticks(media_preco_por_classificacao.index)

    # Adiciona os valores da média nas barras
    for i, v in enumerate(media_preco_por_classificacao.values):
        plt.text(i + 2, v, f'{v:.2f}', ha='center', va='bottom')

    plt.show()