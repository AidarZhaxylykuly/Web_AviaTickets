import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AviamainComponent } from './aviamain.component';

describe('AviamainComponent', () => {
  let component: AviamainComponent;
  let fixture: ComponentFixture<AviamainComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AviamainComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AviamainComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
