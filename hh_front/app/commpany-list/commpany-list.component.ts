import { Component, OnInit } from '@angular/core';
import { CompanyService } from '../company.service';

@Component({
  selector: 'app-commpany-list',
  templateUrl: './commpany-list.component.html',
  styleUrls: ['./commpany-list.component.css']
})
export class CommpanyListComponent implements OnInit {

  public companies = []
  
  constructor(private companiService: CompanyService) { }

  ngOnInit(): void {
    this.companiService.getCompanies().subscribe(companies => {
      this.companies = companies
      console.log(companies)
    })
  }

}