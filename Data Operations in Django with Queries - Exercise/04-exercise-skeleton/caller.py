import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact


# Create queries within functions

def create_pet(name: str, species: str):
    pet = Pet.objects.create(
        name=name,
        species=species
    )

    return f"{name} is a very cute {species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )

    return f"The artifact {name} is {age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.is_magical and artifact.age > 250:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    all_artifacts = Artifact.objects.all()
    for artifact in all_artifacts:
        artifact.delete()


# create_artifact('Ancient Sword',
#                 'Lost Kingdom',
#                 500,
#                 'A legendary sword with a rich history', True)
# create_artifact('Crystal Amulet',
#                 'Mystic Forest',
#                 300,
#                 'A magical amulet believed to bring good fortune', True
#                 )
# create_artifact('Stone Tablet',
#                 'Ruined Temple',
#                 1000,
#                 'An ancient tablet covered in mysterious inscriptions', False
#                 )
#
# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# artifact_object = Artifact.objects.get(name='Ancient Sword')
# rename_artifact(artifact_object, 'Ancient Shield')
# print(artifact_object.name)
