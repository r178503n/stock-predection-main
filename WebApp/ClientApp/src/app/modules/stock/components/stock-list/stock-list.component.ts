import { Component, OnInit } from '@angular/core';
import { interval, Subscription } from 'rxjs';
import { SweetAlertService } from 'src/app/application-shared/services/sweetAlert/sweetAlert.service';
import { StockService } from '../../services/stock.service';

@Component({
  selector: 'app-stock-list',
  templateUrl: './stock-list.component.html',
  styleUrls: ['./stock-list.component.scss'],
})
export class StockListComponent implements OnInit {
  status: any;
  stockList;
  subscription: Subscription;
  isTraining;
  selectedTrain;
  selectedPrediction;
  constructor(
    private stockService: StockService,
    private sweetAlert: SweetAlertService
  ) {}

  ngOnInit() {
    const source = interval(10000);
    this.subscription = source.subscribe((val) => {
      // this.autoRefreshProcessedImagesList();
      console.log('fetching data...!');
    });
    this.getStockList();
  }
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }

  selectPrediction(key){
    this.selectedPrediction =key;
  }

  getStockList(): any {
    this.stockService.getStockList().subscribe(
      (response) => {
        console.log(response);
        this.stockList = response;

        this.sweetAlert.success('data successfully refreshed');
      },
      (error) => {
        console.log(error);

        this.sweetAlert.error('Oops no stocks found yet');
      }
    );
  }

  trainModel(key): any {
    this.isTraining = true;
    this.selectedTrain = key;
    this.stockService.trainModel(key).subscribe(
      (response) => {
        console.log(response);
        this.isTraining = false;
        this.sweetAlert.success('trained model');
      },
      (error) => {
        console.log(error);
        this.isTraining = false;
        this.sweetAlert.error3('Oops failed training model');
      }
    );
  }
}
