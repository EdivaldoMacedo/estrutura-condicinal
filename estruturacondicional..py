renda = 1500

# Primeira condicional com base na renda para definir a variável imposto
if renda > 2500:
    imposto = 500
elif renda >= 1500:  # Nova condicional para ajustar o imposto com base em critérios adicionais
    imposto = 100
else:
    imposto = 50

# Agora, o comando print está corretamente indentado.
print(imposto)