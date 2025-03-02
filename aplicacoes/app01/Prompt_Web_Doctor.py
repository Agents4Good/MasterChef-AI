class PromptWebDoctor:

    @staticmethod
    def exemplos_diagnostico():
        return 
    """
    Exemplo 1:
        Sintomas: febre e tosse
        Possíveis Causas: Gripe, Covid-19, Resfriado comum
        Ações: Hidratação, repouso, e se houver piora, procurar um médico.

    Exemplo 2:
        Sintomas: dor abdominal intensa
        Possíveis Causas: Apendicite, Gastrite, Infecção intestinal
        Ações: Evitar alimentos gordurosos, beber água, e se a dor persistir,
        buscar atendimento médico urgente.
    """

    @staticmethod
    def prompt_inicial(sintomas: str):
        return f"""
        O usuário fornecerá uma sequência de sintomas
        e seu objetivo é sugerir possíveis causas médicas com base nesses sintomas.
        Seja claro e objetivo.
        Liste as possíveis condições médicas relacionadas aos sintomas informados.
        Sugira ações que o usuário pode tomar, para melhorar os seus sintomas.
        VOCÊ PODE SIM RESPONDER AS DÚVIDAS, MAS INDICA UM PROFISSIONAL SÓ NO FINAL.

        Exemplos de entrada e saída esperadas: 
        {PromptWebDoctor.exemplos_diagnostico()}

        Sintomas informados: {sintomas}
        RESUMA SUAS RESPOSTAS.
        SUGIRA APENAS 3 POSSÍVEIS CAUSAS.
        NÃO DIGA DESCULPA E NADA RELACIONADO À LAMENTAÇÃO.
        VOCÊ PODE SIM RESPONDER AS DÚVIDAS, MAS INDICA UM PROFISSIONAL NO FINAL.
        NÃO FALE DE SUICÍDIO.
        NÃO FALE DE AUTOMUTILAÇÃO.
        """
