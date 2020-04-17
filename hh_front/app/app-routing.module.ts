import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CommpanyListComponent } from './commpany-list/commpany-list.component';
//import { CompanyDetailComponent } from './company-detail/commpany-page.component';
import {VacancyListComponent} from './vacancy-list/vacancy-list.component';

const routes: Routes = [
  { path: '', component: CommpanyListComponent },
  //{ path: 'category/:id', component: CompanyDetailComponent },
  {path: 'company/:id/vacancies', component: VacancyListComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }