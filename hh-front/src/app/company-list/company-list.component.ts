import { Component, OnInit } from '@angular/core';
import { CompanyService } from '../company.service';
import {Company} from '../company';
@Component({
  selector: 'app-company-list',
  templateUrl: './company-list.component.html',
  styleUrls: ['./company-list.component.css']
})
export class CompanyListComponent implements OnInit {
companies:Company[];

  constructor() { }

  ngOnInit(): void {
    this.getCompanyList();
  }
  getCompanyList() {
    this.companyService.getCompanyList()
      .subscribe(companies => this.companies = companies);
  }
  deleteCompany(id) {
    this.companyService.deleteCompany(id).subscribe(res => {
      
      this.getCompanyList();
    });
  }

}
