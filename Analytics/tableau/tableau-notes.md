# Tableau Notes 

## Tableau File Types
Workbooks (.twb) – Tableau workbook files have the .twb file extension. Workbooks hold one or more worksheets, plus zero or more dashboards and stories.

Bookmarks (.tbm) – Tableau bookmark files have the .tbm file extension. Bookmarks contain a single worksheet and are an easy way to quickly share your work. For more information, see Save a bookmark(Link opens in a new window).

Packaged Workbooks (.twbx) – Tableau packaged workbooks have the .twbx file extension. A packaged workbook is a single zip file that contains a workbook along with any supporting local file data and background images. This format is the best way to package your work for sharing with others who don’t have access to the original data. For more information, see Packaged Workbooks.

Extract (.hyper) – Tableau extract files have the .hyper extension. Extract files are a local copy of a subset or entire data set that you can use to share data with others, when you need to work offline, and improve performance. For more information, see Extract Your Data.

Data Source (.tds) – Tableau data source files have the .tds file extension. Data source files are shortcuts for quickly connecting to the original data that you use often. Data source files do not contain the actual data but rather the information necessary to connect to the actual data as well as any modifications you've made on top of the actual data such as changing default properties, creating calculated fields, adding groups, and so on. For more information, see Save Data Sources.

Packaged Data Source (.tdsx) – Tableau packaged data source files have the .tdsx file extension. A packaged data source is a zip file that contains the data source file (.tds) described above as well as any local file data such as extract files (.hyper), text files, Excel files, Access files, and local cube files. Use this format to create a single file that you can then share with others who may not have access to the original data stored locally on your computer. For more information, see Save Data Sources.

## Tableau Products
https://onware.com/tableau-product-and-licenses/   

Helping you understand the Tableau license and product list.
Have you ever visited Tableau to find more information about their products? You may have heard of Tableau Creator, Explorer, and Viewer; however, those are not actual products, but rather, role-based licenses. They give you different products and capabilities on the platform. To have the right combination of Tableau’s offerings for you and your organization, it is important to understand the functionalities and limitations of each.

Confused? Don’t worry! We at Onware Business Solutions are tech geeks – in other words, we love technology. However, we never purchase new or existing technologies without first learning about it and fully understanding our needs and requirements. Therefore, we would never recommend or push you to do the same! We believe Tableau is a great investment to see and understand your data; therefore, we want to help explain each Tableau product to help you make the right decision.

### Tableau Desktop
Tableau Desktop allows for authoring of content for visual analytics and data exploration. Perform visual analytics with multiple data sources, using drag and drop actions. Tableau Desktop enables you to explore the data and come up with new, visual, ways to answer important business questions. Furthermore, Desktop provides the capability to create interactive dashboards for guided analytics and stories. It can also publish to a server or online environment so the rest of the organization can leverage your work. This application requires Windows or a Mac computer.

### Tableau Prep
Tableau Prep refers to two products: Prep Builder, to help you build data flows, and Prep Conductor, to schedule, monitor, and manage flows across the organization. Prep’s main purpose is as an ETL (extract, transform, load) tool to get data ready for analysis. It allows you to visually combine data from multiple data sources. Moreover, you can clean data, and publish data sources to serve as a single source of truth for your organization. Prep Builder is locally installed, while Prep Conductor is browser based.


### Tableau Server and Online
Share and collaborate with your organization with Tableau Server and Tableau Online by hosting workbooks, data sources, prep flows, and data extracts published through Tableau Prep or Desktop. Live connections can bring real-time data to Dashboards and workbooks. Otherwise, data extracts can be scheduled to refresh as often as every 15 mins. Furthermore, these products include productivity and efficiency improvements by allowing you to subscribe to a workbook or dashboard. Meaning Tableau can send automated and scheduled emails with your data and a link to your dashboard. Furthermore, Tableau Server/Online can send data alerts when conditions are met – like, when revenue reaches new record highs.


Author inside your browser in Tableau Server or Tableau Online

One of the main differentiators for Tableau Server and Tableau Online is the ability for web and mobile authoring. End-users can not only interact with your data but can also build upon it and create new analysis if they require more information – all within the browser and with similar functionality as Tableau Desktop.

The other differentiator is both Tableau Server and Tableau Online are enterprise business intelligence solutions with data governance and multi-tiered security features. These include network security, data security, authentication, and authorization so different users viewing the same dashboard will see different results based on their permissions. Moreover, Tableau Server and Online can act as a central source of truth by hosting the metadata that your whole organization uses.


User based permissions in Tableau Server and Tableau Online
Tableau Server and Tableau Online are both browser-based products. In addition, a mobile app is available for mobile viewing. Now, you may be asking what is the difference between Tableau Server and Tableau Online?

The customer hosts Tableau Server, either on-premises or a public cloud (such as Microsoft Azure or Amazon AWS). Whereas, Tableau hosts Tableau Online. In other words, Tableau Online is a Software as a Service (SaaS). Meaning, it is easier to start with Tableau Online as organizations do not need to purchase and maintain new hardware. In addition, hardware optimization, upgrades, facility, staff, system monitoring and system availability is all managed and configured by Tableau.

Tableau Server is for or organizations focusing on security and control or has very large data workloads. It gives your organization full control of everything behind the firewall, like the hardware and software. For a more balanced approach, Tableau Server hosted by the public cloud gives your organization full control of the software. Because Tableau manages everything for you on Tableau Online, the cost is slightly higher than Tableau Server.

### Tableau Reader
Tableau Reader is a free tool that opens packaged workbooks which allows you to view the analysis and the underlying data. Exported packaged workbooks contain static data. Unlike the other products, Tableau Reader cannot automate data refreshes. Furthermore, there are no security features on packaged workbooks – such as, password protection.

End users’ functionalities are limited to what is set up for them – like filters and dashboard actions. As a result, self-service analytics for further analysis of unanswered questions is not available in Tableau Reader. This tool is for local install and cannot open on a mobile device. Tableau Reader does not have security features required for many organizations. Therefore, use in the enterprise setting is unlikely. However, its use cases include sharing content with a small amount of people.

### Tableau Public
Tableau Public allows you to share data with the world. However, it must be published through Tableau Desktop. However, instead of exporting a workbook and sending it, you publish it to Tableau Public, Tableau’s free cloud service. Like Tableau Reader, the published data is static and there are no automated data refreshes – unless you are using Google Sheets as a live data connection. Furthermore, it has limited security as it is possible to prevent people from downloading and viewing the underlaying data; however, the published workbook or dashboard is available to everyone that has access to the URL. Tableau Public is browser-based instead of local install and it can be opened on any device including mobile. Typically, the use cases for Public include sharing content with the world, for example, media or government entities that want to show COVID-19 information.

### Tableau Mobile

Tableau Mobile is a free mobile app for accessing Tableau Server and Tableau Online on your mobile devices. While it is free, Mobile requires a Tableau license in order to use it. Tableau Mobile will automatically cache your favourite views and dashboards for offline viewing.

### Embedded Analytics

Embedded Analytics is a specialized version of Tableau Server that integrates Tableau’s powerful BI capabilities directly into your applications, products, and web portals. This offering includes Tableau Server at a reduced rate. However, it has a five data source limit, so it is for very specific use cases.

## Licenses

Tableau offers named, role-based licenses that grant access to a range of products and capabilities on the platform.

### Tableau Viewer
Viewer licenses lets users view and interact with the workbooks created by others in Tableau Server, Tableau Online and Tableau Mobile. This role is assigned to users that want to put data at the centre of their conversations because it allows them to interact with dashboards and visualizations to help make informed decisions. Additional functionalities include giving access to users to add comments to workbooks, export visualizations into various formats, download workbook summary data, create subscriptions, and receive data-driven alerts.

### Tableau Explorer
Explorers are comfortable with data and are often interested beyond the confines of pre-built reports dashboards. These users are likely receiving reports from others and combining them to obtain the answers required for deeper analysis. Explorers have all the functionalities of Tableau Viewer, but also includes the access to workbook creation and authoring capabilities using a web browser or mobile device, as well as a full set of collaboration features.

### Tableau Creator
Tableau Creator includes two products – Tableau Desktop and Tableau Prep Builder – and are for power users in your organization. In other words, they connect to data sources, clean and prepare data, and then conduct complex analysis to create useful reports and dashboards to distribute to others either through emailed workbooks or through Tableau Server or Online. In addition to giving you all the functionalities available under the Explorer license, it also allows users to create and publish new workbooks and dashboards from a new data source, edit embedded data sources in the data pane, and create and publish new data connections.

## Add-Ons
There are also add-on licenses for additional functionality for Tableau Server and Tableau Online.

### Data Management Add-on

#### Tableau Data Management Add-On
Tableau Data Management add-on provides visibility and control of data in your analytics environment on Tableau Server or Tableau Online by ensuring it is up to date and trusted when it is being used for analysis. The add-on includes Tableau Prep Conductor (see above) and Tableau Catalog, which gives you a complete view of all the data being used in Tableau, like how it is being used and how it is connected to your analytics.

### Server Management Add-on

#### Tableau Server Management Add-on
Tableau Server Management add-on provides enhanced security, manageability, and scalability capabilities for Tableau Server. The add-on allows configuration of workload management for optimization, as well as increases security, reliability and scalability when using Amazon’s AWS. Furthermore, it provides a resource tool for a comprehensive look at the health of the Tableau Server to identify issues, and a content migration tool to copy or migrate content between projects.


