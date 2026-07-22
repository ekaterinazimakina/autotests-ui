from components.courses.course_view_component import CourseViewComponent
from components.views.empty_view_components import EmptyViewComponents
from pages.base_page import BasePage

from playwright.sync_api import Page, expect

from navigation.navbar_component import NavbarComponent

from navigation.sidebar_component import SidebarComponent

from components.courses.courses_list_toolbar_view_component import CourseListToolbarViewComponent


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.empty_view = EmptyViewComponents(page, identifier='courses-list')
        self.course_view = CourseViewComponent(page)
        self.toolbar_view = CourseListToolbarViewComponent(page)

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )
