import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddbokComponent } from './addbok.component';

describe('AddbokComponent', () => {
  let component: AddbokComponent;
  let fixture: ComponentFixture<AddbokComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddbokComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddbokComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
