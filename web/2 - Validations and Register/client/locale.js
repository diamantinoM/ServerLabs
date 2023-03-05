export {
    tr,
    trDoc,
    setCurrentLanguage,
    UnknownMessageID,
    UnknownLanguage,
}
/*
    No código HTML, em vez de (por exemplo):

        <h1>Torneio da Primavera</h1>
        OU
        <h1>Spring Tournament</h1>

    colocamos: 

        <h1>{{tr TOURNAMENT_NAME}}</h1>
 */

const userMessages = {
    en_US: {
        ERR_ENROLLING: "We were unable to proceed with the enrollment.",
        ERR_UNSPECIFIED_TOURNAMENT: "We're sorry but there was a problem with the enrolling data.",
        ERR_PLAYER_ALREADY_ENROLLED: "Player already enrolled at the tournament.",
        ERR_UNKNOWN_TOURNAMENT_ID: "We're sorry but there was a problem with the enrolling data.",
        SUCCESS_ENROLLING: "Player successfully enrolled.",
        PLAYER: "Player",
        EMAIL_ADDR: "Email address",
        TOURNAMENT_NAME: "Spring Tournament",
        TOURNAMENT_PRIZES: "Prizes up to 10th place",
        RULES: "Regulation",
        MEMBERS: "Members",
        ENROLL_HERE: "Register for tournament here",
        FULL_NAME_LABEL: "Full name",
        EMAIL_ADDR_LABEL: "Email",
        PHONE_NUMBER_LABEL: "Phone number",
        BIRTH_DATE_LABEL: "Birth date (DD/MM/YYYY)",
        PASSWORD_LABEL: "Password",
        REPEAT_PASSWORD_LABEL: "Password again",
        PLAYER_LEVEL_LABEL: "Level",
        DATE_FMT: "(MM/DD/YYYY)",
        PRIVACY_POLICY_MSG: "I read and I agree with the",
        PRIVACY_POLICY: "Privacy Policy",
        BEGINNER_LEVEL: "Beginner",
        INTERMEDIATE_LEVEL: "Intermediate",
        ADVANCED_LEVEL: "Advanced",
        PRE_PRO_LEVEL: "Pre-professional",
        PRO_LEVEL: "Professional",
        SUBMIT_BTN: "Submit",
        RESET_BTN: "Reset",
        LANGUAGE_OPTION1: "Portuguese",
        LANGUAGE_OPTION2: "English",
        TOURNAMENT_NAME_LABEL: "Tournament",
        SPRING_LEVEL: "Spring",
        SUMMER_LEVEL: "Summer",
        WINTER_LEVEL: "Winter",
        FALL_LEVEL: "Fall",
    },
    pt_PT: {
        ERR_ENROLLING: "Não foi possível concluir a inscrição.",
        ERR_UNSPECIFIED_TOURNAMENT: "Ooops...detectámos um problema com os dados de inscrição.",
        ERR_PLAYER_ALREADY_ENROLLED: "O jogador já se encontra inscrito no torneio.",
        ERR_UNKNOWN_TOURNAMENT_ID: "Ooops...torneio desconhecido.",
        SUCCESS_ENROLLING: "Jogador inscrito com sucesso.",
        PLAYER: "Jogador",
        EMAIL_ADDR: "Endereço de email",
        TOURNAMENT_NAME: "Torneio da Primavera",
        TOURNAMENT_PRIZES: "Prémios até ao 10&#x2070; lugar",
        RULES: "Regulamento",
        MEMBERS: "Membros",
        ENROLL_HERE: "Inscreva-se aqui",
        FULL_NAME_LABEL: "Nome completo",
        EMAIL_ADDR_LABEL: "Email",
        PHONE_NUMBER_LABEL: "Telefone",
        BIRTH_DATE_LABEL: "Data de nascimento",
        PASSWORD_LABEL: "Senha",
        REPEAT_PASSWORD_LABEL: "Senha de novo",
        PLAYER_LEVEL_LABEL: "Nível",
        DATE_FMT: "(DD/MM/AAAA)",
        PRIVACY_POLICY_MSG: "Li e concordo com a",
        PRIVACY_POLICY: "Política de Privacidade",
        BEGINNER_LEVEL: "Iniciado",
        INTERMEDIATE_LEVEL: "Intermédio",
        ADVANCED_LEVEL: "Avançado",
        PRE_PRO_LEVEL: "Pré-profissional",
        PRO_LEVEL: "Profissional",
        SUBMIT_BTN: "Submeter",
        RESET_BTN: "Limpar",
        LANGUAGE_OPTION1: "Português",
        LANGUAGE_OPTION2: "Inglês",
        TOURNAMENT_NAME_LABEL: "Torneio",
        SPRING_LEVEL: "Primavera",
        SUMMER_LEVEL: "Verão",
        WINTER_LEVEL: "Inverno",
        FALL_LEVEL: "Outono",
    },
};

class UnknownMessageID extends Error {}

class UnknownLanguage extends Error {}

let currentLanguage = 'pt_PT';

function setCurrentLanguage(newCurrentLanguage) {
  if (!userMessages[newCurrentLanguage]) {
    throw new UnknownLanguage(`Language ${newCurrentLanguage} is not supported.`);
  }
  currentLanguage = newCurrentLanguage;
} 

function tr(messageID) {
  const message = userMessages[currentLanguage][messageID];
  if (!message) {
    throw new UnknownMessageID(`Message ID ${messageID} is not defined for language ${currentLanguage}.`);
  }
  return message;
} 

const trDoc = (function() {
  const trDocRe = /{{tr\s([^}\s]+)\s*}}/g; 

  return function trDoc(ancestorNode = document) {
    ancestorNode.querySelectorAll('*').forEach(node => {
      node.innerHTML = node.innerHTML.replace(trDocRe, (_, msg) => tr(msg));
    })
  }
})();
      // If you want to replace HTML like this : 
      //
      // '<img src="example.jpg" title="{{tr Example}}"/>' OR '<img src="example.png" alt="{{tr some text}}" />'.
      //
      // Then this function can help. The loop iterates over the title and alt attributes,
      // and replaces their values with the translated version. 
      //
      // for (const attr of ['title', 'alt']) {
      //   if (node.hasAttribute(attr)) {
      //     node.setAttribute(attr, node.getAttribute(attr).replace(trDocRe, (_, msg) => tr(msg)));
      //   }
      // }