import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CommpanyListComponent } from './commpany-list.component';

describe('CommpanyListComponent', () => {
  let component: CommpanyListComponent;
  let fixture: ComponentFixture<CommpanyListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CommpanyListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CommpanyListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
