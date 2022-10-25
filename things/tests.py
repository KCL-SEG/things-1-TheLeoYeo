from django.db import IntegrityError
from django.db.models import Model
from django.forms import ValidationError
from django.test import TestCase

from things.models import Thing


class ThingModelTestCase(TestCase):
    def setUp(self):
        self.thing = Thing(name="James", description="Bob", quantity=0)
        
    def _assert_thing_valid(self):
        try:
            self.thing.full_clean()
        except(ValidationError):
            self.fail("thing should be valid")

      
    def _assert_thing_invalid(self):
        with self.assertRaises(ValidationError):
            self.thing.full_clean()
            
            
    def _assert_valid(self, object:Model):
        try:
            object.full_clean()
        except(ValidationError):
            self.fail("object should be valid")
            
    
    def _assert_invalid(self, object:Model):
        with self.assertRaises(ValidationError):
            object.full_clean()
            
            
    def _assert_raises(self, object:Model, error:Exception):
        with self.assertRaises(error):
            object.full_clean()

        
    def test_valid_thing(self):
        self._assert_thing_valid()
        
    
    def test_blank_name(self):
        self.thing.name=""
        self._assert_thing_invalid()
        
                   
    def test_30_character_name(self):
        self.thing.name="a"*30
        self._assert_thing_valid()
            
            
    def test_bad_31_character_name(self):
        self.thing.name="a"*31
        self._assert_thing_invalid()
        
        
    def test_120_character_description(self):
        self.thing.description="a"*120
        self._assert_thing_valid()
            
            
    def test_bad_121_character_description(self):
        self.thing.description="a"*121
        self._assert_thing_invalid()

       
    def test_non_unique_name(self):
        thing1 = Thing(name="abcd", description="Bob", quantity=0)
        thing2 = Thing(name="abcd", description="James", quantity=100)
        
        self._assert_valid(thing1)
        thing1.save()
        with self.assertRaises(IntegrityError):
            thing2.save()
        
        
    def test_description_can_be_non_unique(self):
        thing1 = Thing(name="abcd", description="James", quantity=0)
        thing2 = Thing(name="abc", description="James", quantity=100)
        
        self._assert_valid(thing1)
       
        self._assert_valid(thing2)
        
        
    def test_quantity_can_be_non_unique(self):
        thing1 = Thing(name="abcd", description="James", quantity=0)
        thing2 = Thing(name="abc", description="Greg", quantity=0)
        
        self._assert_valid(thing1)
        self._assert_valid(thing2)

         
    def test_quantity_can_not_be_negative(self):
        self.thing.quantity = -1
        self._assert_thing_invalid()

           
    def test_quantity_can_not_be_over_100(self):
        self.thing.quantity = 101
        self._assert_thing_invalid()
