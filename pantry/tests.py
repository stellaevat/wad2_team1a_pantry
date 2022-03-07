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

"""
Tests to check the initial structure of templates
"""
class PantryTemplateStructureTests(TestCase):

    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.templates_dir = os.path.join(self.project_base_dir, 'templates')
        self.pantry_templates_dir = os.path.join(self.templates_dir, 'pantry')

    def test_templates_directory_exists(self):
        """
        Does the templates/ directory exist?
        """
        directory_exists = os.path.isdir(self.templates_dir)
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}Your project's templates directory does not exist.{FAILURE_FOOTER}")

    def test_pantry_templates_directory_exists(self):
        """
        Does the templates/pantry/ directory exist?
        """
        directory_exists = os.path.isdir(self.pantry_templates_dir)
        self.assertTrue(directory_exists, f"{FAILURE_HEADER}The Pantry templates directory does not exist.{FAILURE_FOOTER}")

    def test_template_dir_setting(self):
        """
        Does the TEMPLATE_DIR setting exist, and does it point to the right directory?
        """
        variable_exists = 'TEMPLATE_DIR' in dir(settings)
        self.assertTrue(variable_exists, f"{FAILURE_HEADER}Your settings.py module does not have the variable TEMPLATE_DIR defined!{FAILURE_FOOTER}")

        template_dir_value = os.path.normpath(settings.TEMPLATE_DIR)
        template_dir_computed = os.path.normpath(self.templates_dir)
        self.assertEqual(template_dir_value, template_dir_computed, f"{FAILURE_HEADER}Your TEMPLATE_DIR setting does not point to the expected path. Check your configuration, and try again.{FAILURE_FOOTER}")

    def test_template_lookup_path(self):
        """
        Does the TEMPLATE_DIR value appear within the lookup paths for templates?
        """
        lookup_list = settings.TEMPLATES[0]['DIRS']
        found_path = False

        for entry in lookup_list:
            entry_normalised = os.path.normpath(entry)

            if entry_normalised == os.path.normpath(settings.TEMPLATE_DIR):
                found_path = True

        self.assertTrue(found_path, f"{FAILURE_HEADER}Your project's templates directory is not listed in the TEMPLATES>DIRS lookup list. Check your settings.py module.{FAILURE_FOOTER}")

    def test_templates_exist(self):
        """
        Do the base.html and home.html templates exist in the correct place?
        (Maybe add more checks for all html files in templates directory)
        """
        base_path = os.path.join(self.pantry_templates_dir, 'base.html')
        home_path = os.path.join(self.pantry_templates_dir, 'home.html')

        self.assertTrue(os.path.isfile(base_path), f"{FAILURE_HEADER}Your base.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(home_path), f"{FAILURE_HEADER}Your home.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
