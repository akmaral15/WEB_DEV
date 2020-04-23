import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { VacancyListComponent} from './vacancy-list/vacancy-list.component';
import { CompanyListComponent } from './company-list/company-list.component';

const routes: Routes = [
  { path: '', component: CompanyListComponent },
  { path: 'company/:id', component: VacancyListComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
