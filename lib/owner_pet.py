class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self,name,pet_type,owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        # makes the pet object
        Pet.all.append(self) 
        # keeps track of all the pets that are made for the class and adds them to the list

    @property
    def pet_type(self):
        return self._pet_type
        # gets a animal
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception
        self._pet_type = pet_type
        # if the pet type isnt in the list then raise an exception, else the pettype is in the list


class Owner:
    def __init__(self,name):
        self.name = name
        # makes the owner

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    # if the pet in the pet list owner matches the owner return it
    
    def add_pet(self, pet):
      if not isinstance(pet, Pet):
          raise Exception
      pet.owner = self
# if the pet isnt a isinstance of the Pet class raise a Exception, else the the pet is a isinstance of the Pet class so add a owner to that pet

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    # sorts though the list of objects calls a an