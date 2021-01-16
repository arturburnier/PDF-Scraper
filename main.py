# Desenvolvido por Artur Burnier
# imports
import pdfplumber
import re

# Carrega o arquivo PDF
with pdfplumber.open("arquivo.pdf") as pdf:
    pages = pdf.pages
    tabela = []
    concluido = 0
    total_pgs = 0

    for i, pg in enumerate(pages):
        total_pgs = total_pgs+1

# le o arquivo PDF e extrai o texto
    for i, pg in enumerate(pages):
        text = pages[i].extract_text()

# Procura pelo texto no formato indicado abaixo
        regex_cnpj = r"\d{2}[-.\s]?\d{3}[-.\s]?\d{3}[-.\s\/]?\d{4}[-.\s]?\d{2}"
        matches_cnpj = re.finditer(regex_cnpj, text, re.MULTILINE | re.IGNORECASE)

        regex_valor = r"([0-9]+[\.,])?([0-9]+[\,])+([0-9]{2})+($)"
        matches_valor = re.finditer(regex_valor, text, re.MULTILINE | re.IGNORECASE)

# Monta tabela com os valores encontrados
        for matchNum, match_cnpj in enumerate(matches_cnpj, start=0):
            match_cnpj = match_cnpj.group()

            for matchNum1, match_valor in enumerate(matches_valor, start=0):
                match_valor = match_valor.group()
                tabela.append(match_cnpj+";"+match_valor)
                concluido = concluido+1

        # Mostra o andamento
        print("{i} de {total_pgs} - {x:0.2f}%".format(i=i+1, total_pgs=total_pgs, x=(i+1)/total_pgs*100))

# Remove a duplicata de cada folha
sem_duplicados = tabela[::2]

# Escreve o resultado no arquivo texto
with open('output.txt', 'w') as output:
    for i in sem_duplicados:
        output.writelines(i + "\n")
print("\n", "Conversão finalizada -> output.txt")
print("\n", "Desenvolvido por @arturburnier")

# MIT License
# 
# Copyright (c) [year] [fullname]
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
