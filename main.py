from pathlib import Path

output_directory = Path.cwd()

d = {
    "Films": [
        "Le seigneur des anneaux",
        "Harry Potter",
        "Moon",
        "Forrest Gump"
    ],
    "Employes": [
        "Paul",
        "Pierre",
        "Marie"
    ],
    "Exercices": [
        "les_variables",
        "les_fichiers",
        "les_boucles"
    ]
}

for main_folder, sub_folder in d.items():
    for folder in sub_folder:
        path = Path(output_directory) / main_folder / folder
        path.mkdir(exist_ok=True, parents=True)
