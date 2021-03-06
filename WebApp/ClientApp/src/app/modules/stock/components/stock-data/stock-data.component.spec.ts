/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { StockDataComponent } from './stock-data.component';

describe('StockDataComponent', () => {
  let component: StockDataComponent;
  let fixture: ComponentFixture<StockDataComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StockDataComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StockDataComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
