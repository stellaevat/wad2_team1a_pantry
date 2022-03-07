from django.test import TestCase

import os
import importlib
from django.urls import reverse
from django.conf import settings

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

"""
Tests to check the initial project structure
"""
class PantryProjectStructureTests(TestCase):

    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.pantry_app_dir = os.path.join(self.project_base_dir, 'pantry')

    def test_project_created(self):
        """
        Tests whether the wad2_team1a_pantry configuration directory is present and correct.
        """
        directory_exists = os.path.isdir(os.path.join(self.project_base_dir, 'wad2_team1a_pantry'))
        urls_module_exists = os.path.isfile(os.path.join(self.project_base_dir, 'wad2_team1a_pantry', 'urls.py'))

        self.assertTrue(directory_exists, f"{FAILURE_HEADER}Your wad2_team1a_pantry configuration directory doesn't seem to exist.{FAILURE_FOOTER}")
        self.assertTrue(urls_module_exists, f"{FAILURE_HEADER}Your project's urls.py module does not exist.{FAILURE_FOOTER}")

    def test_pantry_app_created(self):
        """
        Determines whether the Pantry app has been created.
        """
        directory_exists = os.path.isdir(self.pantry_app_dir)
        is_python_package = os.path.isfile(os.path.join(self.pantry_app_dir, '__init__.py'))
        views_module_exists = os.path.isfile(os.path.join(self.pantry_app_dir, 'views.py'))

        self.assertTrue(directory_exists, f"{FAILURE_HEADER}The pantry app directory does not exist.{FAILURE_FOOTER}")
        self.assertTrue(is_python_package, f"{FAILURE_HEADER}The pantry directory is missing files.{FAILURE_FOOTER}")
        self.assertTrue(views_module_exists, f"{FAILURE_HEADER}The pantry directory is missing files.{FAILURE_FOOTER}")

    def test_pantry_has_urls_module(self):
        """
        Did you create a separate urls.py module for Pantry?
        """
        module_exists = os.path.isfile(os.path.join(self.pantry_app_dir, 'urls.py'))
        self.assertTrue(module_exists, f"{FAILURE_HEADER}The pantry app's urls.py module is missing.{FAILURE_FOOTER}")

    def test_is_pantry_app_configured(self):
        """
        Did you add the new Pantry app to your INSTALLED_APPS list?
        """
        is_app_configured = 'pantry' in settings.INSTALLED_APPS

        self.assertTrue(is_app_configured, f"{FAILURE_HEADER}The pantry app is missing from your setting's INSTALLED_APPS list.{FAILURE_FOOTER}")
