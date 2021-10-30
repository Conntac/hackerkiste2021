const numberFormatter = new Intl.NumberFormat(undefined, {
  style: "currency",
  currency: "EUR",
});

export function eurosToString(value: number): string {
  return numberFormatter.format(value);
}
