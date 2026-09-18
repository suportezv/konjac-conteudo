/**
 * Paleta e tokens da Konjac Massa para o Remotion.
 *
 * Nao existe manual de marca no Drive da agencia (conferido em 18/set/2026).
 * Os tres valores marcados "medido" vieram do logotipo oficial
 * (Material - Agencias / Logotipo / logotipo-konjac-massa-mf.png): roxo em
 * 64% dos pixels opacos, aqua em 15%, branco em 14%. Os demais sao derivados
 * desses tres e ficam PENDENTE confirmar com a cliente.
 *
 * Os nomes dos tokens sao o contrato com Aurora.tsx e CartaoTitulo.tsx e nao
 * mudam de estudio para estudio; so os valores mudam.
 */
export const marca = {
  /** Roxo do logotipo (medido). E o acento: palavra em destaque e mancha principal da aurora. */
  rosaVivo: "#802078",
  /** Roxo mais fechado (derivado). */
  rosa: "#6A1A63",
  /** Roxo claro, do tom secundario do logotipo (derivado). */
  rosaSuave: "#B088A8",
  /** Roxo medio para a segunda mancha da aurora (derivado). */
  violeta: "#985890",
  /** Aqua do logotipo (medido). */
  ciano: "#A8D8D8",
  /** Aqua mais saturado (derivado). */
  azulNeon: "#7FD0D0",
  /** Roxo profundo para fundos escuros (derivado). */
  azulProfundo: "#4A1547",
  fundoEscuro: "#1A0A18",
  superficie: "#2A1228",
  /** Branco do logotipo (medido): base clara dos fundos aurora. */
  auroraBase: "#F8F8F8",
  /** Tinta do texto sobre a aurora clara. */
  tinta: "#2A1228",
  /** Fonte da marca: PENDENTE. Sem rede no render, fonte web cai para a sans do sistema. */
  fonte: '"Inter Tight", system-ui, -apple-system, sans-serif',
} as const;
