/**
 * Tokens da Konjac Massa® para o Remotion.
 *
 * Valores oficiais, de `assets/brand/BRAND.md` e do artifact "Konjac Massa
 * Design System" (https://claude.ai/artifact/PYtJR5b7YsjzHRBZUAAq9Z); cópia
 * dos tokens em `design-system/tokens.json`. Não são medições: se a paleta
 * mudar, atualizar os tres lugares.
 *
 * As CHAVES sao o contrato com Aurora.tsx e CartaoTitulo.tsx e vem do template
 * dos estudios irmaos, por isso alguns nomes nao descrevem a cor da Konjac. O
 * nome oficial de cada uma esta no comentario. Trocar os valores muda o visual
 * inteiro sem encostar nos componentes.
 */
export const marca = {
  /** Roxo Konjac: primaria da marca e acento padrao do lettering. */
  rosaVivo: "#812779",
  /** Site, roxo profundo. */
  rosa: "#9a1f7e",
  /** Site, roxo suave. */
  rosaSuave: "#aa4f86",
  /** Site, roxo mais violeta. */
  violeta: "#7f2595",
  /** Menta: secundaria da marca, onda do logo. */
  ciano: "#a8dcda",
  /** Menta do site. */
  azulNeon: "#8cdbd7",
  /** Verde institucional das embalagens. */
  azulProfundo: "#004c28",
  /** Tinta da marca, tambem usada como fundo escuro. */
  fundoEscuro: "#2b2130",
  /** Card do estudio. */
  superficie: "#fdfcfa",
  /** Fundo do estudio: base clara dos fundos aurora. */
  auroraBase: "#f6f3f0",
  /** Tinta: texto sobre fundo claro. */
  tinta: "#2b2130",
  /**
   * Display do estudio. Barlow Condensed e o substituto web da Helvetica Neue
   * Condensed Black; Archivo e o corpo. Fonte remota nao carrega no render
   * (ver gotcha no CLAUDE.md): para usar de verdade, baixar o arquivo para
   * remotion/public/ e carregar com staticFile numa FontFace.
   */
  fonte: '"Barlow Condensed", "Archivo", system-ui, -apple-system, sans-serif',
} as const;
