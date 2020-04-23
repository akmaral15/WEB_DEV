import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CompanyService } from '../company.service';
import {Company} from '../company';
import { Location } from '@angular/common';
import {Vacancy} from '../vacancy';
import {VacancyService} from '../vacancy.service';
@Component({
  selector: 'app-vacancy-list',
  templateUrl: './vacancy-list.component.html',
  styleUrls: ['./vacancy-list.component.css']
})
export class VacancyListComponent implements OnInit {
  company: Company;

  vacancies: Vacancy[];

  constructor(private companyService: CompanyService,
    private vacancyService: VacancyService,
    private route: ActivatedRoute,
    private location: Location) { }

ngOnInit(): void {
this.getCompany();
this.getVacanciesByCompanyId();
}

getCompany() {
const id = +this.route.snapshot.paramMap.get('id');
this.companyService.getCompany(id).subscribe(company => this.company = company);
}
goBack(): void {
this.location.back();
}

getVacanciesByCompanyId() {
const id = +this.route.snapshot.paramMap.get('id');
this.vacancyService.getVacanciesByCompanyId(id)
.subscribe(vacancies => this.vacancies = vacancies);
}

}

