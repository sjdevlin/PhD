from presenters.base_presenter import BasePresenter
from presenters.formulation_presenter import FormulationPresenter
from presenters.plate_presenter import PlatePresenter
from models.formulation_list_model import FormulationListModel
from models.formulation_detail_model import FormulationDetailModel
from views.formulation_list_view import FormulationListView
from views.formulation_detail_view import FormulationDetailView
from database.formulation_store import FormulationListStore, FormulationDetailStore
from database.plate_store import PlateStore
from models.generic_list_model import GenericListModel
from views.generic_list_view import GenericListView
from views.plate_detail_view import PlateDetailView

class MainPresenter(BasePresenter):
    def __init__(self, view, db):
        self.view = view
        self.db = db
        self.view.component_button.config(command=self.show_component)
        self.view.formulation_button.config(command=self.show_formulation)
        self.view.annealing_button.config(command=self.show_annealing)
        self.view.experiment_button.config(command=self.show_experiment)
        self.view.material_button.config(command=self.show_material)
        self.view.plate_button.config(command=self.show_plate)
        self.view.buffer_button.config(command=self.show_buffer)
        self.view.camera_button.config(command=self.show_camera)
        self.view.camera_setting_button.config(command=self.show_camera_setting)
        self.view.microscope_button.config(command=self.show_microscope)

    def show_formulation(self):
        formulation_list_store = FormulationListStore(self.db)
        formulation_list_model = FormulationListModel(formulation_list_store)
        formulation_list_view = FormulationListView(self.view.info_frame)

        formulation_detail_store = FormulationDetailStore(self.db)
        formulation_detail_model = FormulationDetailModel(formulation_detail_store)
        formulation_detail_view = FormulationDetailView(self.view.detail_frame)

        formulation_presenter = FormulationPresenter(formulation_list_view, formulation_detail_view, formulation_list_model, formulation_detail_model)

    def show_camera(self):
        pass

    def show_camera_setting(self):
        pass

    def show_material(self):
        pass

    def show_buffer(self):
        pass

    def show_plate(self):
        plate_store = PlateStore(self.db)
        plate_list_model = GenericListModel(plate_store)
        plate_list_view = GenericListView(self.view.info_frame,['ID','PLATE', 'DESC'])

        plate_detail_view = PlateDetailView(self.view.detail_frame)
        plate_presenter = PlatePresenter(plate_list_view, plate_detail_view, plate_list_model)

    def show_microscope(self):
        pass

    def show_component(self):
        component_store = ComponentStore(self.db)
        component_model = ComponentModel(component_store)
        component_view = ComponentView(self.view.info_frame)
        component_presenter = ComponentPresenter(component_view, component_model)

    def show_experiment(self):
        pass

    def show_annealing(self):
        pass
