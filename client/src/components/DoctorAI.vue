<!-- Reference : https://bootstrap-vue.org/ -->
<!-- DoctorAI Page Styling starts -->
<template>
    <!-- Creates a overlay to show the user that a backend process is running -->
    <b-overlay :show="showProcess" rounded="sm">  
        <!-- Container to hold all UI display elements -->
        <!-- <b-container class="bv-example-row"> -->
            <b-container class="dr-ai-ui">
            <b-row>
                <b-col>
                    <div>
                        <!-- Display success message when the data from source is loaded to local database and the success message auto-disappears  -->
                        <transition name="fade">
                            <p class="alert alert-success" role="alert" v-if="showMessage">
                                <strong>Success.</strong> {{message}}
                            </p>
                        </transition>
                    </div>  
                    
                    <div>                           
                        <b-card header-tag="header" footer-tag="footer">
                            <!-- Header used as border design -->
                            <template #header>
                                <b-card-img src="/src/assets/image2.jpg" alt="Image" fluid style="max-height: 10px;"></b-card-img>
                            </template>
                            <!-- Page title, subtitle and Image styling  -->
                            <b-card no-body>                
                                <b-row no-gutters>
                                    <b-col fluid="sm" sm="3">
                                        <b-card-img src="/src/assets/image1.jpg" alt="Image" class="rounded-0"></b-card-img>
                                    </b-col>
                                    <b-col fluid="sm" sm="6">
                                        <b-card-title title-tag="h2">
                                            Doctor.AI
                                        </b-card-title>
                                        <b-card-sub-title>
                                            Looking for medication information. Doctor AI is here to help!!!
                                        </b-card-sub-title>           
                                    </b-col>
                                </b-row>
                            </b-card>
                            <!-- Medication list data display design -->
                            <b-card no-body>
                                <b-tabs card content-class="mt-3" fill>
                                    <template #tabs-end>
                                        <li role="presentation" class="nav-item align-self-center"> Currently displaying <strong>{{btnValue}}</strong> Medication type </li>
                                    </template>
                                    <b-tab title="Medication List" active> 
                                        <b-row>
                                            <b-col fluid="md" md="8">
                                                <!-- Displaying each medication type as button and on buttton click get requested data -->
                                                <b-card-text><strong>Choose the Medication Type : </strong>
                                                    <b-button pill variant="outline-primary" @click="getMedicationByType('Over-the-counter')">Over-the-counter</b-button>
                                                    <b-button pill variant="outline-info" @click="getMedicationByType('Prescription')">Prescription</b-button>
                                                    <b-button pill variant="outline-secondary" @click="getMedicationByType('Discontinued')">Discontinued</b-button>
                                                </b-card-text>
                                            </b-col>
                                            <b-col fluid>
                                                <!-- Displaying button to refresh data and on buttton click refresh the data -->
                                                <button 
                                                    type="button"
                                                    class="btn btn-success btn-sm"
                                                    @click="refreshData">
                                                    Refresh data again? click Me
                                                </button>
                                            </b-col>
                                        </b-row>
                                        <b-container fluid="sm" sm="2">
                                            <b-row fluid="sm" sm="1">
                                                <b-col>
                                                    <b-container fluid="sm" sm="2">
                                                        <!-- User Interface controls -->
                                                        <b-row>
                                                            <!-- UI element to Sort the displayed data -->
                                                            <b-col lg="6" class="my-1">
                                                                <b-form-group
                                                                    label="Sort By"
                                                                    label-for="sort-by-select"
                                                                    label-cols-sm="3"
                                                                    label-align-sm="right"
                                                                    label-size="sm"
                                                                    class="mb-0"
                                                                    v-slot="{ ariaDescribedby }"
                                                                >
                                                                    <b-input-group size="sm">
                                                                        <b-form-select
                                                                            id="sort-by-select"
                                                                            v-model="sortBy"
                                                                            :options="sortOptions"
                                                                            :aria-describedby="ariaDescribedby"
                                                                            class="w-75"
                                                                        >
                                                                            <template #first>
                                                                                <option value="">-- none --</option>
                                                                            </template>
                                                                        </b-form-select>

                                                                        <b-form-select
                                                                            v-model="sortDesc"
                                                                            :disabled="!sortBy"
                                                                            :aria-describedby="ariaDescribedby"
                                                                            size="sm"
                                                                            class="w-25"
                                                                        >
                                                                            <option :value="false">Asc</option>
                                                                            <option :value="true">Desc</option>
                                                                        </b-form-select>
                                                                    </b-input-group>
                                                                </b-form-group>
                                                            </b-col>
                                                            <!-- UI element to filter the displayed data -->                                                    
                                                            <b-col lg="6" class="my-1">
                                                                <b-form-group
                                                                    label="Filter"
                                                                    label-for="filter-input"
                                                                    label-cols-sm="3"
                                                                    label-align-sm="right"
                                                                    label-size="sm"
                                                                    class="mb-0"
                                                                >
                                                                    <b-input-group size="sm">
                                                                        <b-form-input
                                                                            id="filter-input"
                                                                            v-model="filter"
                                                                            type="search"
                                                                            placeholder="Type to Search"
                                                                        >
                                                                        </b-form-input>

                                                                        <b-input-group-append>
                                                                            <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
                                                                        </b-input-group-append>
                                                                    </b-input-group>
                                                                </b-form-group>
                                                            </b-col>                                    
                                                            <hr>
                                                        </b-row>
                                                        <!-- Main table element -->
                                                        <b-table
                                                            :items="items"
                                                            :fields="fields"
                                                            :current-page="currentPage"
                                                            :per-page="perPage"
                                                            :filter="filter"
                                                            :filter-included-fields="filterOn"
                                                            v-model:sort-by="sortBy"
                                                            v-model:sort-desc="sortDesc"
                                                            :sort-direction="sortDirection"
                                                            stacked="md"
                                                            show-empty
                                                            small
                                                            @filtered="onFiltered"
                                                        >
                                                            <template #cell(name)="row">
                                                                {{ row.value.first }} {{ row.value.last }}
                                                            </template>

                                                            <template #cell(actions)="row">
                                                                <b-button size="sm" @click="info(row.item, row.index, $event.target)" class="mr-1">
                                                                    More Details
                                                                </b-button>
                                                            </template>
                                                            <template #row-details="row">
                                                                <b-card>
                                                                    <ul>
                                                                        <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
                                                                    </ul>
                                                                </b-card>
                                                            </template>
                                                        </b-table>
                                                        <!-- UI element to filter number of records displayed per page -->
                                                        <b-row>
                                                            <b-col sm="7" md="6" class="my-1">
                                                                <b-form-group
                                                                    class="mb-0"
                                                                >
                                                                    <b-form-select
                                                                        id="per-page-select"
                                                                        v-model="perPage"
                                                                        :options="pageOptions"
                                                                        size="sm"
                                                                    >
                                                                    </b-form-select>
                                                                </b-form-group>
                                                            </b-col>
                                                            <!-- UI element for pagination-->
                                                            <b-col fluid sm="7" md="6" class="my-1">
                                                                <b-pagination
                                                                    v-model="currentPage"
                                                                    :total-rows="totalRows"
                                                                    :per-page="perPage"
                                                                    align="fill"
                                                                    size="sm"
                                                                    class="my-0"
                                                                    first-text="First"
                                                                    prev-text="Prev"
                                                                    next-text="Next"
                                                                    last-text="Last"                                        
                                                                >
                                                                </b-pagination>
                                                            </b-col>
                                                        </b-row>                                    
                                                        <hr>
                                                        <!-- UI element to display more additonal info -->
                                                        <b-modal :id="infoModal.id" :title="infoModal.title" ok-only @hide="resetInfoModal">
                                                            <div>
                                                                <b-table-simple hover small caption-top responsive>
                                                                    <caption><b>More Details:</b></caption>
                                                                    <b-tbody>
                                                                        <b-tr v-for="(value, key) in infoModal.data" :key="key">
                                                                            <b-td style="text-transform:capitalize;"><b>{{ key.replaceAll('_',' ') }}</b></b-td>
                                                                            <b-td>{{ value[0]}}</b-td>
                                                                        </b-tr>
                                                                    </b-tbody>
                                                                </b-table-simple>
                                                            </div>
                                                        </b-modal>
                                                    </b-container>                                
                                                </b-col>
                                            </b-row>
                                            <b-row>
                                                <!-- pie chart display -->
                                                <b-col>
                                                    <div class="chart-container column">
                                                        <plotlychart :chart="piechart"></plotlychart>
                                                    </div>                                
                                                </b-col>
                                                <!-- bar chart display -->
                                                <b-col>
                                                    <div class="chart-container column">
                                                        <plotlychart :chart="barchart"></plotlychart>
                                                    </div>                        
                                                </b-col>
                                            </b-row>
                                        </b-container>
                                    </b-tab>
                                    <!-- Disclaimer info display tab -->
                                    <b-tab title="Before Proceeding review this DISCLAIMER" class="font-weight-bold ">
                                        <b-row>
                                            <b-col >
                                                <b-card>
                                                    <b-card-text>
                                                        <h3>By using this web application you agree to this Disclaimer:</h3> <br>
                                                        Before trying any medication listed here always speak to your health provider about the risks and benefits of any medication listed here. <br>
                                                        Do not rely on this data which is pulled from the open FDA to make decisions regarding medical care. Please read FDA Terms of Service @https://open.fda.gov/terms/.<br>
                                                        Any FDA warning, not limited to the one listed below on the FDA site should always adhered. <br>FDA warning provides privacy and security notices consistent with applicable federal laws, directives, and other federal guidance for accessing this Government system, which includes all devices/storage media attached to this system. This system is provided for Government-authorized use only. Unauthorized or improper use of this system is prohibited and may result in disciplinary action and/or civil and criminal penalties. At any time, and for any lawful Government purpose, the government may monitor, record, and audit your system usage and/or intercept, search and seize any communication or data transiting or stored on this system. Therefore, you have no reasonable expectation of privacy. Any communication or data transiting or stored on this system may be disclosed or used for any lawful Government purpose.
                                                    </b-card-text>     
                                                </b-card>  
                                            </b-col> 
                                        </b-row>
                                    </b-tab>
                                </b-tabs>
                            </b-card>
                            <!-- Footer used as border design -->
                            <template #footer>
                                <b-card-img src="/src/assets/image2.jpg" alt="Image" fluid style="max-height: 10px;"></b-card-img>
                            </template>
                        </b-card>    
                    </div>         
                </b-col>
            </b-row>
        </b-container>
        <!-- overlay message to display when backend processing is happening -->
        <template #overlay>
            <div class="text-center">
                <p id="wait-label">Please wait...</p>
            </div>
        </template>
    </b-overlay>
</template>
<!-- DoctorAI Page Styling Ends -->
<!-- DoctorAI Page Scripting Starts   -->
<script>
    import axios from 'axios';
    import PlotlyChart from './PlotlyChart.vue';

    export default {
    data() 
    // defines and returns the properties of UI elements
    {   
        return {
            // Main table properties
            btnValue:"",
            showMessage: false,
            showProcess: false,
            items: [],
            dosageformchart: [],
            intakeroutechart: [],
            fields: [
            { key: 'brand_name', label: 'Medication', sortable: true, sortDirection: 'desc' },
            { key: 'dosage_form', label: 'Dosage Form', sortable: true, class: 'text-left' },
            { key: 'route', label: 'Intake Route', sortable: true, class: 'text-left' },
            { key: 'active_ingredients', label: 'Active Ingredients/Strength', sortable: true, class: 'text-left' },
            { key: 'actions', label: 'Additional Info' }
            ],
            // number records per page display properties
            totalRows: 1,
            currentPage: 1,
            perPage: 5,
            pageOptions: [{ value: 5, text: "Display 5 records per page" }, { value: 10, text: "Display 10 records per page" }],
            sortBy: '',
            sortDesc: false,
            sortDirection: 'asc',
            filter: null,
            filterOn: [],
            infoModal: {
            id: 'info-modal',
            title: '',
            content: '',
            data: {}
            },
            // bar chart properties
            barchart: {
                uuid: "123",
                traces: [
                {
                    x: [],                
                    y: [],
                    line: {
                    color: "#5e9e7e",
                    width: 4,
                    shape: "line"
                    },
                    type: "bar",
                    rotation: 90
                    
                }
                ],
                layout: {
                    title:'Medication Count By Intake Route',
                }
            },
            // pichart properties
            piechart: {
                uuid: "321",
                traces: [                    
                    {
                        labels: [],                
                        values: [],
                        line: {
                        color: "#5e9e7e",
                        width: 10,
                        shape: "line"
                        },
                        type: "pie",
                        showlegend: true,
                        rotation: 90,
                        texttemplate:"%{percent:.0%f}",
                        textposition:"inside"
                    
                    }
                ],
                layout: {
                    title:'Medication Count By Dosage Form',
                }
            }
            
        }
    },
    computed: {
      sortOptions() {
        // Create an options list from our fields
        return this.fields
          .filter(f => f.sortable)
          .map(f => {
            return { text: f.label, value: f.key }
          })
      },
    },
    mounted() {
      // Set the initial number of items
      this.totalRows = this.items.length
      this.refreshData();
      this.getMedicationByType('Over-the-counter')   
    },
    components: {
        // Set the PlotlyChart component
        plotlychart: PlotlyChart,
    }, 
    // method to do FLASK API calls to get data from backend server   
    methods: { 
       // FLASK API call to get additional info details when requested by user
      info(item, index, button) {
            this.showProcess = true;
            const path = `http://localhost:5001/getMoreDetailsFromFDA/"${item.brand_name}"`;
            axios.get(path)
            .then((response) => {         
                this.infoModal.title = `${item.brand_name}`
                this.infoModal.content = JSON.stringify(response.data, null, 2)
                this.infoModal.data = response.data
                this.$root.$emit('bv::show::modal', this.infoModal.id, button)
                this.showProcess = false;
            })
            .catch((error) => {
                console.error(error);
                this.showProcess = false;
            }); 
        },
        // rest additional info details when closed
      resetInfoModal() {
            this.infoModal.title = ''
            this.infoModal.content = ''
      },
      // action when filter is applied
      onFiltered(filteredItems) {
            this.totalRows = filteredItems.length
            this.currentPage = 1
      },
      // FLASK API call to refersh back end data
      refreshData() {
        this.showProcess = true;
        const path = 'http://localhost:5001/refresh_data';
        axios.post(path)
            .then((response) => {         
            this.message = response.data;
            this.showMessage = true;
            this.showProcess = false;
            setTimeout(() => { this.showMessage = false; }, 5000);
            })
            .catch((error) => {
            console.error(error);
            this.showProcess = false;
            });        
        },
        // FLASK API call to retrive medication and cound infomration based on the medication type selected by the user
        getMedicationByType(medicationType){
            this.btnValue=medicationType
            this.showProcess = true;
            const path = `http://localhost:5001/getMedicationByType/${medicationType}`;
            axios.get(path)
            .then((response) => {         
            this.items = response.data[0].products;
            this.totalRows = response.data[0].products.length;
            })
            .catch((error) => {
            console.error(error);
            this.showProcess = false;
            });   
            const pathDosage = `http://localhost:5001/getCountByCategory/${medicationType}/dosage_form`;
            axios.get(pathDosage)
            .then((response) => {         
            this.piechart.traces[0].labels = []
            this.piechart.traces[0].values = []

            this.dosageformchart = response.data;
            this.dosageformchart.forEach((x) => {
                this.piechart.layout.datarevision = new Date().getTime();
                this.piechart.traces[0].labels.push(x.dosage_form);
                this.piechart.traces[0].values.push(x.count);                                   
            });
            })
            .catch((error) => {
            console.error(error);
            this.showProcess = false;
            }); 
            const pathIntake = `http://localhost:5001/getCountByCategory/${medicationType}/route`;
            axios.get(pathIntake)
            .then((response) => {         
            this.barchart.traces[0].x = []
            this.barchart.traces[0].y = []
            
            this.intakeroutechart = response.data;
            this.intakeroutechart.forEach((x) => {
                this.barchart.layout.datarevision = new Date().getTime();
                this.barchart.traces[0].x.push(x.route);
                this.barchart.traces[0].y.push(x.count);                                   
                this.showProcess = false;                                                                         
            });                      
            })
            .catch((error) => {
            console.error(error);
            this.showProcess = false;
            }); 
        }      
    }
  }
</script>
<!-- DoctorAI Page Scripting Ends   -->