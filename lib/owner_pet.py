class Pet:
    PET_TYPES =  ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, new_type):
        if not isinstance(new_type, str) or new_type not in Pet.PET_TYPES:
            raise Exception("not a valid pet type")
        self._pet_type = new_type

        

class Owner:
    def __init__(self, name="John"):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("not a valid pet")
    # def get_sorted_pets(self):
    #     return sorted(self.pets(), key=Pet.get_pet_name)

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)