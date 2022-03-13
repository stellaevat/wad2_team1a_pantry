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
        Checks that all html files are located in the templates directory
        """
        base_path = os.path.join(self.pantry_templates_dir, 'base.html')
        home_path = os.path.join(self.pantry_templates_dir, 'home.html')
        tabs_path = os.path.join(self.pantry_templates_dir, 'tabs.html')

        check_email_path = os.path.join(self.pantry_templates_dir, 'check_email.html')
        sign_in_path = os.path.join(self.pantry_templates_dir, 'sign_in.html')
        sign_up_path = os.path.join(self.pantry_templates_dir, 'sign_up.html')

        user_profile_path = os.path.join(self.pantry_templates_dir, 'user_profile.html')
        edit_profile_path = os.path.join(self.pantry_templates_dir, 'edit_profile.html')

        add_recipe_path = os.path.join(self.pantry_templates_dir, 'add_recipe.html')
        add_recipe_ingredients_path = os.path.join(self.pantry_templates_dir, 'add_recipe_ingredients.html')
        ingredient_selection_path = os.path.join(self.pantry_templates_dir, 'ingredient_selection.html')
        recipe_display_grid_path = os.path.join(self.pantry_templates_dir, 'recipe_display_grid.html')

        search_by_ingredient_path = os.path.join(self.pantry_templates_dir, 'search_by_ingredient.html')
        search_results_path = os.path.join(self.pantry_templates_dir, 'search_results.html')

        show_category_path = os.path.join(self.pantry_templates_dir, 'show_category.html')
        show_my_recipes_path = os.path.join(self.pantry_templates_dir, 'show_my_recipes.html')
        show_recipe_path = os.path.join(self.pantry_templates_dir, 'show_recipe.html')
        show_starred_recipes_path = os.path.join(self.pantry_templates_dir, 'show_starred_recipes.html')

        self.assertTrue(os.path.isfile(base_path), f"{FAILURE_HEADER}Your base.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(home_path), f"{FAILURE_HEADER}Your home.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(tabs_path), f"{FAILURE_HEADER}Your tabs.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")

        self.assertTrue(os.path.isfile(check_email_path), f"{FAILURE_HEADER}Your check_email.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(sign_in_path), f"{FAILURE_HEADER}Your sign_in.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(sign_up_path), f"{FAILURE_HEADER}Your sign_up.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")

        self.assertTrue(os.path.isfile(user_profile_path), f"{FAILURE_HEADER}Your user_profile.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(edit_profile_path), f"{FAILURE_HEADER}Your edit_profile.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")

        self.assertTrue(os.path.isfile(add_recipe_path), f"{FAILURE_HEADER}Your add_recipe.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(add_recipe_ingredients_path), f"{FAILURE_HEADER}Your add_recipe_ingredients.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(ingredient_selection_path), f"{FAILURE_HEADER}Your ingredient_selection.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(recipe_display_grid_path), f"{FAILURE_HEADER}Your recipe_display_grid.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")

        self.assertTrue(os.path.isfile(search_by_ingredient_path), f"{FAILURE_HEADER}Your search_by_ingredient.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(search_results_path), f"{FAILURE_HEADER}Your search_results.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")

        self.assertTrue(os.path.isfile(show_category_path), f"{FAILURE_HEADER}Your show_category.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(show_my_recipes_path), f"{FAILURE_HEADER}Your show_my_recipes.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(show_recipe_path), f"{FAILURE_HEADER}Your show_recipe.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(show_starred_recipes_path), f"{FAILURE_HEADER}Your show_starred_recipes.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")

"""
Tests to checks the configuration of the database
"""
class PantryDatabaseConfigurationTests(TestCase):

    def setUp(self):
        pass

    def does_gitignore_include_database(self, path):
        """
        Takes the path to a .gitignore file, and checks to see whether the db.sqlite3 database is present in that file.
        """
        f = open(path, 'r')

        for line in f:
            line = line.strip()

            if line.startswith('db.sqlite3'):
                return True

        f.close()
        return False

    def test_databases_variable_exists(self):
        """
        Does the DATABASES settings variable exist, and does it have a default configuration?
        """
        self.assertTrue(settings.DATABASES, f"{FAILURE_HEADER}Your project's settings module does not have a DATABASES variable.{FAILURE_FOOTER}")
        self.assertTrue('default' in settings.DATABASES, f"{FAILURE_HEADER}You do not have a 'default' database configuration in your project's DATABASES configuration variable.{FAILURE_FOOTER}")

    def test_gitignore_for_database(self):
        """
        If you are using a Git repository and have set up a .gitignore, checks to see whether the database is present in that file.
        """
        git_base_dir = os.popen('git rev-parse --show-toplevel').read().strip()

        if git_base_dir.startswith('fatal'):
            warnings.warn("You don't appear to be using a Git repository for your codebase.")
        else:
            gitignore_path = os.path.join(git_base_dir, '.gitignore')

            if os.path.exists(gitignore_path):
                self.assertTrue(self.does_gitignore_include_database(gitignore_path), f"{FAILURE_HEADER}Your .gitignore file does not include 'db.sqlite3' -- you should exclude the database binary file from all commits to your Git repository.{FAILURE_FOOTER}")
            else:
                warnings.warn("You don't appear to have a .gitignore file in place in your repository.")
