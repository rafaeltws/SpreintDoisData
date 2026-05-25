# ChargeGrid Intelligence – Sprint 2

Sistema inteligente de gerenciamento de recarga de veículos elétricos desenvolvido em Python.

O projeto simula um ambiente comercial de carregamento elétrico, permitindo múltiplas sessões simultâneas, controle de potência, tarifação dinâmica e integração simulada com protocolos como OCPP e MODBUS.

---

# Funcionalidades

- Gerenciamento de múltiplas sessões de recarga
- Controle inteligente de distribuição de energia
- Tarifação dinâmica
- Simulação de comunicação OCPP/MODBUS
- Relatórios gerais das sessões
- Menu interativo no terminal
- Simulação de recarga em tempo real

---

# Tecnologias Utilizadas

- Python 3
- Biblioteca `random`
- Biblioteca `time`

---

# Estrutura do Sistema

O sistema possui:

- Cadastro de sessões
- Simulação de recarga
- Controle automático de potência
- Encerramento de sessões
- Relatório geral
- Simulação de integração externa

---

# Como Executar

## 1. Instale o Python

Baixe em:

```txt
https://www.python.org/downloads/
```

---

## 2. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

---

## 3. Entre na pasta do projeto

```bash
cd nome-do-projeto
```

---

## 4. Execute o sistema

```bash
python main.py
```

ou

```bash
python3 main.py
```

---

# Exemplo do Sistema Rodando

```txt
====== MENU ======
1 - Nova sessão
2 - Simular recarga
3 - Finalizar sessão
4 - Relatório
5 - Sair

Opção: 1

Nova sessão
Nome: Rafael
Tipo (comum/premium): premium
Horario atual: 19

Controle de energia ativado
Sessão iniciada
```

---

# Controle Inteligente de Energia

O sistema possui um limite total de potência:

```python
limiteEnergia = 40
```

Quando vários veículos estão conectados:

- A potência é dividida automaticamente
- O sistema evita sobrecarga
- O carregamento é redistribuído entre os veículos ativos

Exemplo:

- 1 veículo → 40 kW
- 2 veículos → 20 kW para cada
- 4 veículos → 10 kW para cada

---

# Tarifação Dinâmica

A tarifa muda dependendo de:

- Horário da recarga
- Quantidade de veículos conectados
- Tipo do usuário

## Regras

### Horário de pico

Entre:

```txt
18h até 22h
```

A tarifa aumenta.

---

### Alta demanda

Se houver 3 ou mais veículos conectados:

```txt
Taxa adicional aplicada
```

---

### Usuário premium

Usuários premium recebem desconto.

---

# Simulação OCPP / MODBUS

O sistema simula integração com plataformas externas através de mensagens como:

```txt
[OCPP]
Enviando dados...
```

e

```txt
[MODBUS]
Dados recebidos
```

---

# Estrutura das Sessões

Cada sessão armazena:

```python
{
    "nome": nomeUsuario,
    "tipo": tipoUsuario,
    "horario": horarioAtual,
    "energia": 0,
    "potencia": 0,
    "status": "Carregando"
}
```

---

# Critérios do Sprint Atendidos

| Critério | Status |
|---|---|
| Múltiplas sessões | ✅ |
| Controle de demanda | ✅ |
| Tarifação dinâmica | ✅ |
| Simulação OCPP/MODBUS | ✅ |
| Estrutura lógica | ✅ |
| Interatividade | ✅ |
| Robustez geral | ✅ |

---

# Melhorias Futuras

- Interface gráfica
- Banco de dados
- Login de usuários
- Histórico de sessões
- Dashboard em tempo real
- Integração real com APIs
- Controle individual de carregadores

---

# Autor

Projeto desenvolvido para o Sprint 2 – ChargeGrid Intelligence.
