class GeneLab:
    def __init__(self) -> None:
        self.genes: dict[str, list] = {}

    def inject_gene(self, subject_id: str, gene_name: str) -> None:
        if subject_id not in self.genes:
            self.genes[subject_id] = []
        self.genes[subject_id].append(gene_name)

    def check_compatibility(self, subject_id: str) -> bool:
        subject_genes = self.genes.get(subject_id)
        return not ('cyborg' in subject_genes and 'organic' in subject_genes)


_lab = GeneLab()
inject_gene = _lab.inject_gene
check_compatibility = _lab.check_compatibility
